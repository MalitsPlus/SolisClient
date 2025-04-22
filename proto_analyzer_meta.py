import re
from pathlib import Path

cs_file = "cache/dump.cs"
out_file_enum = "cache/penum.proto"
out_file_master = "cache/pmaster.proto"
out_file_api = "cache/papi.proto"
out_file_transaction = "cache/ptransaction.proto"
original_str: str

# Enum Patterns
enum_ptn = r"Solis.Common.Proto\n(?P<content>[\s\S]+?)// Namespace:"
enum_name_ptn = r"public enum (?P<name>\w+)"
enum_properties_ptn = r"public const \w+ (?P<k>\w+) = (?P<v>\d+);"

# Common Patterns
common_name_ptn = r"public sealed class (?P<name>\w+)"
common_properties_ptn = r"public const int (?P<fieldName>\w+) = (?P<value>\d+);[\s\S]*?private (readonly )?(?P<type>[\w<>]+) (?P<name>\w+);"

# Master patterns
master_ptn = r"Solis.Common.Proto.Master\n(?P<content>[\s\S]+?)// Namespace:"
# Api patterns 
api_ptn = r"Solis.Common.Proto.Api\n(?P<content>[\s\S]+?)// Namespace:"
# Transaction patterns
transaction_ptn = r"Solis.Common.Proto.Transaction\n(?P<content>[\s\S]+?)// Namespace:"

# Service patterns
srv_cls_ptn = r"// Namespace: \npublic class \w+\.\w+Client : ClientBase\<[\s\S]+?\n}\n\n// Namespace"
srv_srv_ptn = r"public class (?P<serviceName>\w+)\.\w+Client : ClientBase\<"
srv_clm_ptn = r"public virtual (?P<responseName>\w+) (?P<methodName>\w+)\((?P<requestName>\w+) request,.+Metadata"

# Pairs & Generations
enum_pairs = "  {ename} = {v};\n"
enum_text = """enum {name} {
{pairs}}
"""

common_pairs = "  {type} {name} = {value};\n"
common_text = """message {name} {
{pairs}}
"""

outter_text = """syntax = "proto3";
{imports}
{contents}
"""

type_dict = {
    "double": "double",
    "float": "float",
    "int": "int32",
    "long": "int64",
    "uint": "uint32",
    "ulong": "uint64",
    "bool": "bool",
    "string": "string",
    "ByteString": "bytes"
}
def get_type(cs_type: str) -> str:
    if cs_type not in type_dict.keys():
        return cs_type
    return type_dict[cs_type]

def gen_enum(name, properties) -> str:
    pairs = ""
    for it in properties:
        pairs += enum_pairs.replace("{k}", it[0]).replace("{v}", it[1]).replace("{ename}", f"{name}_{it[0]}")
    return enum_text.replace("{name}", name).replace("{pairs}", pairs)

def analyze_enum() -> str:
    m = re.findall(enum_ptn, original_str)
    txt = ""
    for it in m:
        m = re.search(enum_name_ptn, it)
        if m:
            name = m.group("name")
            properties = re.findall(enum_properties_ptn, it)
            txt += gen_enum(name, properties)
    return outter_text.replace("{imports}", "package penum;\noption go_package = \"vibbit/solis/proto/penum\";\n").replace("{contents}", txt)

def gen_common(name: str, properties: list) -> str:
    pairs = ""
    for ppt in properties:
        pairs += common_pairs.replace("{value}", ppt["value"]).replace(
            "{type}", ppt["type"]).replace("{name}", ppt["name"])
    return common_text.replace("{name}", name).replace("{pairs}", pairs)

def analyze_common(common_ptn: str) -> str:
    m = re.findall(common_ptn, original_str)
    txt = ""
    for one_class in m:
        m_name = re.search(common_name_ptn, one_class)
        if m_name:
            name = m_name.group("name")
            finded_all = re.findall(common_properties_ptn, one_class)
            ppts = []
            for field_name, value,  _, type_, name_ in finded_all:
                type_ = get_type(type_)
                name_ = name_.strip("_")

                m_repeated = re.search(
                    r"RepeatedField<(?P<t_name>\w+)>", type_)
                if m_repeated:
                    type_ = f"repeated {get_type(m_repeated.group(1))}"
                ppts.append({"field_name": field_name,
                            "value": value, "type": type_, "name": name_})
            txt += gen_common(name, ppts)
    if common_ptn == api_ptn:
        imports = 'package api;\noption go_package = "vibbit/solis/proto/papi";\nimport "penum.proto";\nimport "pmaster.proto";\nimport "ptransaction.proto";\n'
    elif common_ptn == master_ptn:
        imports = 'package pmaster;\noption go_package = "vibbit/solis/proto/pmaster";\nimport "penum.proto";\n'
    elif common_ptn == transaction_ptn:
        imports = 'package ptransaction;\noption go_package = "vibbit/solis/proto/ptransaction";\nimport "penum.proto";\n'
    return outter_text.replace("{imports}", imports).replace("{contents}", txt)


enum_lst: list[str]
master_lst: list[str]
api_lst: list[str]
trans_lst: list[str]

def rplc_func(mobj: re.Match) -> str:
    c_type = mobj.group(0)
    if c_type in type_dict.values():
        return c_type
    if c_type in enum_lst:
        return f"penum.{c_type}"
    elif c_type in trans_lst:
        return f"ptransaction.{c_type}"
    elif c_type in api_lst:
        return f"api.{c_type}"
    elif c_type in master_lst:
        return f"pmaster.{c_type}"
    else:
        raise

def add_packages():
    global enum_lst
    global master_lst
    global api_lst
    global trans_lst

    enm_ptn = r"enum (?P<e_type>\w+) {"
    enum_lst = re.findall(enm_ptn, Path(out_file_enum).read_text(encoding="utf8"))

    cmn_ptn = r"message (?P<c_type>\w+) {"  

    master_txt = Path(out_file_master).read_text(encoding="utf8")
    master_lst = re.findall(cmn_ptn, master_txt)

    api_txt = Path(out_file_api).read_text(encoding="utf8")
    api_lst = re.findall(cmn_ptn, api_txt)

    trans_txt = Path(out_file_transaction).read_text(encoding="utf8")
    trans_lst = re.findall(cmn_ptn, trans_txt)

    kv_ptn = r"\w+(?= \w+ \= \d+;)"

    n_txt = re.sub(kv_ptn, rplc_func, master_txt)
    # deals special cases
    n_txt = n_txt.replace("api.ExerciseDeckPosition", "pmaster.ExerciseDeckPosition")
    Path(out_file_master).write_text(n_txt)

    n_txt = re.sub(kv_ptn, rplc_func, api_txt)
    Path(out_file_api).write_text(n_txt)

    n_txt = re.sub(kv_ptn, rplc_func, trans_txt)
    Path(out_file_transaction).write_text(n_txt)
    
def get_services() -> str: 
    txt = "message Empty {}\n"
    m = re.findall(srv_cls_ptn, original_str)
    for one_class in m:
        srv_match = re.search(srv_srv_ptn, one_class)
        if srv_match:
            srv_name = srv_match.group("serviceName")
            txt += "service " + srv_name + " {\n"
            clm_matches = re.findall(srv_clm_ptn, one_class)
            for clm in clm_matches:
                resp_name = clm[0]
                metd_name = clm[1]
                req_name = clm[2]
                txt += f"  rpc {metd_name}({req_name}) returns ({resp_name});\n"
            txt += "}\n"
    return txt


if __name__ == "__main__":
    original_str = Path(cs_file).read_text(encoding="utf-8")
    enm_txt = analyze_enum()
    Path(out_file_enum).write_text(enm_txt, encoding="utf-8")
    master_txt = analyze_common(master_ptn)
    Path(out_file_master).write_text(master_txt, encoding="utf-8")
    api_txt = analyze_common(api_ptn)
    service_txt = get_services()
    Path(out_file_api).write_text(api_txt + service_txt, encoding="utf-8")
    transaction_txt = analyze_common(transaction_ptn)
    Path(out_file_transaction).write_text(transaction_txt, encoding="utf-8")
    add_packages()
    # api_txt = analyze_api()
    # Path(out_file_api).write_text(api_txt, encoding="utf-8")
