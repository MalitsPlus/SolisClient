#

from pathlib import Path
import shutil
import json
import filecmp
from google.protobuf.json_format import MessageToDict

_SEPARATORS = (",", ":")
_MASTER_DIR = "masterdata"
_OUT_DIR = "cache/update_master"

used_files = [
    "Card",
    "CardParameter",
    "CardRarity",
    "Character",
    "CharacterGroup",
    "Quest",
    "Music",
    "MusicChartPattern",
    "LiveBonusGroup",
    "LiveBonus",
    "LiveAbility",
    "MarathonQuest",
    "Setting",
    "Skill",
    "SkillEfficacy",
    "SkillTarget",
    "SkillTrigger",
    "PvpQuest",
    "GvgQuest",
    "LeagueQuest",
    "RaidQuest",
]


def backup_old_files():
    Path(_OUT_DIR).mkdir(exist_ok=True)
    for file in used_files:
        source = f"{_MASTER_DIR}/{file}.json"
        pth = Path(source)
        if pth.exists():
            shutil.copyfile(pth, f"{_OUT_DIR}/{file}.json")


# minify json from _MASTER_DIR and dump it to _OUT_DIR ("cache/update_master")
def minify_json(file: str):
    source = f"{_MASTER_DIR}/{file}.json"
    pth = Path(source)
    if pth.exists():
        with open(pth, "r", encoding="utf8") as fp:
            json_obj = json.load(fp)
            with open(f"{_OUT_DIR}/{file}.json", "w", encoding="utf8") as fw:
                json.dump(json_obj, fw, ensure_ascii=False, separators=_SEPARATORS)


def update_master_jsons() -> bool:
    Path(_OUT_DIR).mkdir(exist_ok=True)
    need_update = False
    for file in used_files:
        source = f"{_MASTER_DIR}/{file}.json"
        pth = Path(source)
        if pth.exists():
            out_ptn = Path(f"{_OUT_DIR}/{file}.json")
            if out_ptn.exists():
                is_same = filecmp.cmp(pth, f"{_OUT_DIR}/{file}.json")
                # For test
                # is_same = False
                if is_same:
                    continue
            minify_json(file)
            need_update = True
        else:
            out_ptn = Path(f"{_OUT_DIR}/{file}.json")
            minify_json(file)
            need_update = True
    return need_update


def prepare_battles():
    files = ["PvpQuest", "LeagueQuest", "GvgQuest", "RaidQuest"]
    for file in files:
        pth = Path(f"ipr-master-diff/{file}.json")
        if pth.exists():
            shutil.copyfile(pth, f"{_OUT_DIR}/{file}.json")
        else:
            pth = Path(f"{_OUT_DIR}/{file}.json")
            if pth.exists():
                continue
            else:
                pth.touch(exist_ok=False)
                pth.write_text("[]")


def check_and_dump_json(file: str, proto: any) -> bool:
    pth_str = f"{_OUT_DIR}/{file}.json"
    pth = Path(pth_str)
    quest_json: list[dict] = json.loads(pth.read_text(encoding="utf8"))
    for quest in quest_json:
        if quest["id"] == proto.id:
            return False
    proto_dict = MessageToDict(
        proto, use_integers_for_enums=True, always_print_fields_with_no_presence=True
    )
    quest_json.insert(0, proto_dict)
    pth.write_text(
        json.dumps(quest_json, ensure_ascii=False, indent=2), encoding="utf8"
    )
    shutil.copyfile(pth, f"{_MASTER_DIR}/{file}.json")
    return True


def update_battles(proto: any, _type: str) -> bool:
    need_update = False
    if _type == "pvp":
        need_update |= check_and_dump_json("PvpQuest", proto.topResult.pvpQuest)
    elif _type == "league":
        need_update |= check_and_dump_json(
            "LeagueQuest", proto.seasonInfo.deckABattleQuestInfo
        )
        need_update |= check_and_dump_json(
            "LeagueQuest", proto.seasonInfo.deckBBattleQuestInfo
        )
        need_update |= check_and_dump_json(
            "LeagueQuest",
            proto.seasonInfo.nextSeasonDeckABattleQuestInfo,
        )
        need_update |= check_and_dump_json(
            "LeagueQuest",
            proto.seasonInfo.nextSeasonDeckBBattleQuestInfo,
        )
    elif _type == "gvg":
        need_update |= check_and_dump_json("GvgQuest", proto.topResult.gvgQuest)
    elif _type == "raid":
        need_update |= check_and_dump_json("RaidQuest", proto.marathonInfo.raidQuest)
    return need_update


if __name__ == "__main__":
    backup_old_files()
    update_master_jsons()
