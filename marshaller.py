import time
import gzip
import hashlib
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from google.protobuf.json_format import MessageToDict
import json

_UNIX_1970 = 621355968000000000
_KEY = b"AJRnFaOnOj"


def _get_tick_bytes() -> bytes:
    ticks = int(time.time() * 10000000 + _UNIX_1970)
    result = ticks.to_bytes(8, byteorder="little", signed=False)
    return result


def _make_header(tick_bytes: bytes) -> bytes:
    len1_b = (len(tick_bytes) + 2).to_bytes(1, byteorder="little", signed=False)
    len2_b = len(tick_bytes).to_bytes(1, byteorder="little", signed=False)
    result = len1_b + b"\x00\x00" + len2_b + tick_bytes
    return result


def _strip_raw(raw: bytes) -> tuple[bytes, bytes, bool]:
    header_len = raw[3]
    is_compressed = raw[2] == 1
    header = raw[4 : 4 + header_len]
    body = raw[4 + header_len :]
    return header, body, is_compressed


def _encrypt(plain: bytes, iv: bytes) -> bytes:
    key = hashlib.md5(_KEY).digest()
    iv = hashlib.md5(iv).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.encrypt(pad(plain, block_size=16, style="pkcs7"))
    return result


def _decrypt(enc: bytes, iv: bytes) -> bytes:
    key = hashlib.md5(_KEY).digest()
    iv = hashlib.md5(iv).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = unpad(cipher.decrypt(enc), block_size=16, style="pkcs7")
    return result


def serialize(proto_bytes: bytes) -> bytes:
    if proto_bytes.__len__() == 0:
        return proto_bytes
    tick_bytes = _get_tick_bytes()
    header = _make_header(tick_bytes)
    body = _encrypt(proto_bytes, _KEY + tick_bytes)
    traffic = header + body
    return traffic


def deserialize(raw: bytes) -> bytes:
    if raw.__len__() == 0:
        return raw
    header, body, is_compressed = _strip_raw(raw)
    plain = _decrypt(body, _KEY + header)
    if is_compressed:
        plain = decompress(plain)
    return plain


def decompress(compressed_bytes: bytes) -> bytes:
    return gzip.decompress(compressed_bytes)


def manual_deserialize(raw: bytes) -> bytes:
    raw = raw[5:]
    return deserialize(raw)


if __name__ == "__main__":
    raw = Path("C:/Users/Malits/Desktop/flows/CardEnhanceResp").read_bytes()
    plain = manual_deserialize(raw)
    import papi_pb2 as papi__pb2

    response = papi__pb2.CardEnhanceResponse.FromString(plain)
    jsondict = MessageToDict(
        response,
        use_integers_for_enums=True,
        always_print_fields_with_no_presence=True,
    )
    jsonstr = json.dumps(jsondict, ensure_ascii=False, indent=2)

    with open("cache/temp.json", "w", encoding="utf-8") as fp:
        json.dump(jsondict, fp, ensure_ascii=False, indent=2)

    print(jsonstr)
    a = 1
