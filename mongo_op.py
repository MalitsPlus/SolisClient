import asyncio
import json
from pathlib import Path
import time
import rich_console as console
from solis_client import SolisClient
import mongo_db

MASTER_DIR = "masterdata"
battle_dbs = ["PvpQuest", "LeagueQuest", "GvgQuest", "RaidQuest"]


def gather_master_to_doc_array(version: str) -> list[str]:
    dir = Path(MASTER_DIR)
    doc_array = []
    start_time = time.time_ns() // 1000000
    for file in dir.glob("*.json"):
        name = file.name.removesuffix(".json")
        if name in battle_dbs:
            continue
        # if name == "Reward":
        #     # Reward.json is too large can lead to plan exceeding error
        #     continue
        with file.open("r", encoding="utf8") as fp:
            json_obj = json.load(fp)
            json_str = json.dumps(json_obj, ensure_ascii=False, separators=(",", ":"))
            doc_obj = {
                "name": name,
                "version": version,
                "time": start_time,
                "data": json_str,
            }
            doc_array.append(doc_obj)
            console.info(f"(Mongo) Added '{name}' to doc array.")
    return doc_array


def get_one_battle_doc(name: str) -> str:
    start_time = time.time_ns() // 1000000
    file = Path(MASTER_DIR + "/" + name + ".json")
    if not file.exists():
        return
    with file.open("r", encoding="utf8") as fp:
        json_obj = json.load(fp)
        json_str = json.dumps(json_obj, ensure_ascii=False, separators=(",", ":"))
        doc_obj = {"name": name, "time": start_time, "data": json_str}
        return doc_obj


async def check_version_and_push_to_mongodb(uri: str, client: SolisClient):
    if not client.master_updated and not client.battle_updated:
        console.info("(Mongo) Nothing updated, skip pushing.")
        return
    sem = asyncio.Semaphore(10)
    await mongo_db.init(uri)
    if client.master_updated:
        console.info("(Mongo) Masterdata updating detected, pushing to Atlas...")
        doc_array = gather_master_to_doc_array(client.master_tag.version)
        await mongo_db.push_many_db(doc_array)
        await mongo_db.update_version(mongo_db.version, client.master_tag.version)
        await mongo_db.delete_all_old_docs(mongo_db.version, client.master_tag.version)
        console.info("(Mongo) Masterdata updating completed.")
    if client.battle_updated:
        console.info("(Mongo) Battle data updating detected, pushing to Atlas...")
        tasks = set()
        for name in battle_dbs:
            battle_doc = get_one_battle_doc(name)
            task = asyncio.create_task(
                mongo_db.replace_or_insert_one(sem, name, battle_doc)
            )
            tasks.add(task)
        await asyncio.wait(tasks, timeout=120)
        console.info("(Mongo) Battle data updating completed.")


if __name__ == "__main__":

    async def mainloop():
        async def coro(i: int):
            await asyncio.sleep(3)
            print(f"{i} done")

        tasks = set()
        for i in range(5):
            task = asyncio.create_task(coro(i))
            tasks.add(task)
            print(f"added {i} to tasks")

        await asyncio.wait(tasks, timeout=10)
        print("this is the lastline")

    asyncio.run(mainloop())
