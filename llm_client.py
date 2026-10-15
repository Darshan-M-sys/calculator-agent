from ollama import chat
model= "qwen3:4b"
from definition import tools
def ask_LLM(messages):
    response=chat(
        model=model,
        messages=messages,
         tools=tools
    )
   
    return response

