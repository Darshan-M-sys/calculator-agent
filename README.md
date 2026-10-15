# Math Calculator Agent

This project is a small local AI agent that answers math-related questions using an LLM and a calculator tool. It is built around the Ollama Python client and demonstrates how to connect a model to a function-calling workflow so the assistant can perform arithmetic operations instead of guessing numbers.

## What this project does

The app lets a user type a prompt such as:

- `What is 12 * 8 + 5?`
- `Calculate 100 / (4 + 1)`
- `Solve 3^2 + 7`

The agent sends the message to an Ollama model, and if the request is mathematical, it uses the `calculate` tool to evaluate the expression safely. The result is then returned to the user.

## Project structure

- `main.py` - entry point for the CLI app
- `agent.py` - system prompt and conversation flow for the agent
- `llm_client.py` - wrapper around the Ollama chat API
- `definition.py` - tool definitions exposed to the LLM
- `tool_executor.py` - executes the selected tool call
- `tools/calculator.py` - actual calculator function used for math evaluations

## How it works

1. The user enters an input in the terminal.
2. `main.py` calls `run_agent()` from `agent.py`.
3. The agent appends the user message to its conversation history.
4. `ask_LLM()` sends the latest messages to the Ollama model with the available tool list.
5. If the model decides a calculation is needed, it calls the `calculate` tool.
6. `tool_executor.py` runs the matching function.
7. The tool result is sent back to the model, and the final answer is returned to the user.

## Setup

### 1. Install Python dependencies

If you are using the project virtual environment, activate it first:

```bash
venv\Scripts\activate
```

Then install the required Python package:

```bash
pip install ollama
```

### 2. Install and run Ollama

Make sure Ollama is installed and running on your machine. Then pull the model used by the app:

```bash
ollama pull qwen3:4b
```

## Run the project

From the project root:

```bash
python main.py
```

Then type a math question and press Enter.

## Example

```text
Enter something to calculate: What is 5 * (12 + 4) / 2

42
```

## Notes

- This project is a simple demonstration of tool-using agents.
- The calculator uses Python's `eval()` for expression evaluation, which is fine for a small local demo but should be treated carefully in more production-grade systems.
- It currently focuses on arithmetic and math expression solving, not a broad general-purpose assistant.

## Future improvements

Possible improvements include:

- safer expression validation
- support for more math functions
- improved handling of non-math user requests
- adding more tools beyond calculations
- better prompt engineering and error handling
