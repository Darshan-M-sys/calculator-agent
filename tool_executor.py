from definition import tool_map
from tools.calculator import calculate

def tool_execution(tool_name,parameters):
    try:
       if tool_name in tool_map:
           return tool_map[tool_name](**parameters)

    except Exception as e:
        return e

