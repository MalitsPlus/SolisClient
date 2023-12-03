# Written by ovv

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys

DEFAULT_PACKAGE_NAME = "game.qualiarts.idolypride"


def find_version(html: str) -> str:
    soup = BeautifulSoup(html, features="lxml")
    target_items = list(
        filter(lambda x: "key: 'ds:5'" in x.decode_contents(), soup.find_all("script"))
    )
    if len(target_items) == 0:
        return None
    target = target_items[0].decode_contents()
    js_data = target.replace("AF_initDataCallback(", "")[:-1]
    # [[['3.5.3']], [[[33]], [[[24, '7.0']]]]],
    match = re.search('\[\[\["([\d.]+)"\]\],\[\[\[\d+\]\]\,\[\[\[\d+,"', js_data)
    if match is None:
        return None
    return match.group(1)


def get_version(package_name: str = DEFAULT_PACKAGE_NAME):
    url = f"https://play.google.com/store/apps/details?id={package_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }
    request = Request(url, headers=headers)
    resp = urlopen(request).read()
    return find_version(resp)


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 2:
        print(get_version(argv[1]))
    else:
        print(get_version(DEFAULT_PACKAGE_NAME))
