from json import load
from pathlib import Path

this = Path(__file__).parent
tools = []
for json_file in this.glob("tools/*.json"):
    print(json_file.relative_to(this))
    with json_file.open("r", encoding="utf-8") as f:
        temp = load(f)
        temp["function"]["parameters"]["properties"]["next_function"]={
            "type":"string",
            "description":"下一个要调用的函数的名称"
        }
        tools.append(temp)
