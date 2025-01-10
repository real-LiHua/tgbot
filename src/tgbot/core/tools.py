from json import load
from pathlib import Path

this = Path(__file__).parent
tools = []
for json_file in this.glob("tools/*.json"):
    print(json_file.relative_to(this))
    with json_file.open("r", encoding="utf-8") as f:
        temp = load(f)
        temp["function"]["parameters"]["properties"]["next_function"] = {
            "type": "string",
            "description": "下一个要调用的函数的函数名称，该名称必须正确且必须存在，要么就留空或保持默认",
        }
        tools.append(temp)

tool_names = {i["function"]["name"] for i in tools}
