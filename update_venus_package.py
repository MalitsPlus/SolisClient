# Copy databases from "cache/update_master" to VenusSysLib and update package version

import json
from pathlib import Path
import shutil

REPO_NAME = "VenusSysLib"
SOURCE_DIR = "cache/update_master"
DEST_DIR = f"{REPO_NAME}/database"
PACKAGE_FILE = f"{REPO_NAME}/package.json"

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
    "MarathonQuest",
    "Setting",
    "Skill",
    "SkillEfficacy",
    "SkillTarget",
    "SkillTrigger",
    # "PvpQuest",
    # "GvgQuest",
    # "LeagueQuest",
]

def main():
    try:
        for file in used_files:
            pth = Path(f"{SOURCE_DIR}/{file}.json")
            if pth.exists():
                shutil.copyfile(pth, f"{DEST_DIR}/{file}.json")
        package_json = json.loads(Path(PACKAGE_FILE).read_text())
        version_splits = str(package_json["version"]).split(".")
        version_splits[-1] = str(int(version_splits[-1]) + 1)
        new_version = ".".join(version_splits)
        package_json["version"] = new_version
        Path(PACKAGE_FILE).write_text(json.dumps(package_json, indent=2))
        print("0")
    except:
        print("1")


if __name__ == "__main__":
    main()
