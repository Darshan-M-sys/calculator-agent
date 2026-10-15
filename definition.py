from tools.calculator import calculate
tool_map={
"calculate":calculate,
}
tools=[
  {
  "type": "function",
  "function": {
    "name": "calculate",
    "description": "Evaluates a mathematical expression string using a secure Python eval approach. Supports basic arithmetic, order of operations, and parentheses.",
    "parameters": {
      "type": "object",
      "properties": {
        "expression": {
          "type": "string",
          "description": "The mathematical expression to evaluate, such as '2 * (15 + 35) / 4'. Avoid any variable assignments or string formatting."
        }
      },
      "required": ["expression"]
    }
  }
}
,
]