import requests
from solis_client import SolisClient

def main():
    # For network testing
    r = requests.get("https://google.co.jp")
    if r.status_code != 200:
        raise "Failed to pass network testing."

    with SolisClient() as client:
        # Run login scenarios to emulate login
        client.run_login_scenarios()
        # Generate notice list json
        client.generate_notice_json()
        # Update masterdata if new version is found
        client.update_master(notify_kv=True)
        # Update octo if new revision is found
        # client.update_octo()

if __name__ == "__main__":
    main()
