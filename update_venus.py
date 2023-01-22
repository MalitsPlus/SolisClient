from pathlib import Path
import shutil
import json
import filecmp

_SEPARATORS = (',', ':')
_MASTER_DIR = "masterdata"
_OUT_DIR = "cache"

used_files = [
    "Card",
    "CardParameter",
    "CardRarity",
    "Character",
    "Quest",
    "Music",
    "MusicChartPattern",
    "LiveBonusGroup",
    "LiveBonus",
    "LiveAbility",
    # "PvpQuest",
    # "GvgQuest",
    # "LeagueQuest",
    "Setting",
    "Skill",
    "SkillEfficacy",
    "SkillTarget",
    "SkillTrigger",
]

def backup_old_files():
    for file in used_files:
        source = f"{_MASTER_DIR}/{file}.json"
        pth = Path(source)
        if pth.exists():
            shutil.copyfile(pth, f"{_OUT_DIR}/{file}.json")

def minify_json(file: str):
    source = f"{_MASTER_DIR}/{file}.json"
    pth = Path(source)
    if pth.exists():
        with open(pth, "r", encoding="utf8") as fp:
            json_obj = json.load(fp)
            with open(f"{_OUT_DIR}/{file}.json", "w", encoding="utf8") as fw:
                json.dump(json_obj, fw, ensure_ascii=False, separators=_SEPARATORS)

def update_files() -> bool:
    need_update = False
    for file in used_files:
        source = f"{_MASTER_DIR}/{file}.json"
        pth = Path(source)
        if pth.exists():
            is_same = filecmp.cmp(pth, f"{_OUT_DIR}/{file}.json")
            if is_same:
                continue
            else:
                minify_json(file)
                need_update = True
    return need_update


if __name__ == "__main__":
    backup_old_files()
    update_files()
