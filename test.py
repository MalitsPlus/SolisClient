import json
import requests
from pathlib import Path
import rich_console as console
import ptransaction_pb2 as transp
import pmaster_pb2 as masp
from cache_manager import set_cache, get_cache
from request_base import send_request
from sqlcipher3 import dbapi2 as sqlcipher
from google.protobuf.json_format import MessageToDict, ParseDict, Parse

def main():
    try:
        conn = sqlcipher.connect(f"cache/gkms/IdolCard")
        sqlcipher
        conn.execute(f"pragma key=\"x'4b31313642704b6b344b514c49386b42674e436a6179544e6f3642714c79436b'\"")
        # conn.execute(f"pragma key=\"\"")
        conn.commit()
        all_data = conn.execute(f"select data from IdolCard;").fetchall()
        msg_list = list[dict]()
        for it in all_data:
            # one_data is a single element tuple 
            one_data = it[0]
            Path("cache/IdolCard_dec.bin").write_bytes(one_data)
    except Exception as e:
        console.error(f"Failed to decipher database 'IdolCard'.")
        console.error(str(e))
    finally:
        conn.close()

if __name__ == "__main__":
    main()
