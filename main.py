import json
import argparse
import requests
import cache_manager
from pathlib import Path
import rich_console as console
import upload
from solis_client import SolisClient

_CACHE_DIR = "cache"
_ARTIFACT_DIR = "masterdata"

def restore_cache(refresh_token: str):
    cache_dir = Path(_CACHE_DIR)
    artifact_dir = Path(_ARTIFACT_DIR)
    # mk cache dir
    cache_dir.mkdir(exist_ok=True)
    artifact_dir.mkdir(exist_ok=True)
    # check client_cache.json
    cache_file = cache_dir.joinpath("client_cache.json")
    if not cache_file.exists():
        cache_json = json.dumps({
            "appVersion": "",
            "masterVersion": "",
            "octoCacheRevision": 1772,
            "refreshToken": refresh_token,
            "idToken": "",
            "firebaseAuthToken": ""
        }, indent=2)
        cache_file.write_text(cache_json)
    with cache_file.open("r") as fp:
        client_cache = json.load(fp)
    # refreshToken MUST NOT be empty 
    assert client_cache["refreshToken"] != ""
    cache_manager.init()

def main():
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", type=str, default="", help="Your firebase refreshToken.")
    parser.add_argument("--kvauth", type=str, default="", help="KV server auth token.")
    parser.add_argument("--kvurl", type=str, default="", help="KV server endpoint.")
    args = parser.parse_args()

    # Restore caches
    restore_cache(args.token)

    # For network testing
    r = requests.get("https://google.co.jp")
    if r.status_code != 200:
        raise "Failed to pass network testing."

    with SolisClient() as client:
        # Run login scenarios to emulate login
        client.run_login_scenarios()
        # Generate notice list json
        client.generate_notice_json()
        # If kvauth and kvurl are given, notify the server to update data
        if args.kvauth != "" and args.kvurl != "":
            # Set secret args
            upload.set_config(kvtoken=args.kvauth, kvurl=args.kvurl)
            # Update masterdata if new version is found
            client.update_master(notify_kv=True)
            # Update notices inconditionaly
            client.put_notice()
        # Update octo if new revision is found
        # client.update_octo()
    console.info("Tasks all done.")

if __name__ == "__main__":
    main()
