from llm_client import ask_LLM
from tool_executor import tool_execution

messages=[
  {
    "role": "system",
    "content": (
      "You are a precise and helpful calculation assistant. "
      "Your primary responsibility is to answer arithmetic and math-related questions accurately. "
      "Use the available calculator tool for numerical evaluation whenever the user asks for a calculation or expression. "
      "When a tool call is needed, choose the correct tool and return the final result clearly and concisely. "
      "Do not guess numeric answers; compute them using the tool when required. "
      "If the user asks a non-math question, respond politely and briefly, and only use tools when relevant. "
      "Keep your final answer easy to read, with the result stated clearly and without unnecessary extra commentary."
    )
  },

]

def run_agent(user):
    messages.append({
    "role":'user',
    'content':user
  })
    while True:
        response=ask_LLM(messages.copy())
        if response["message"]["content"]:
            return response["message"]["content"]
           
        if response['message']["tool_calls"]:
            tools=response['message']["tool_calls"]
            for tool in tools:
                result=tool_execution(tool_name=tool['function']['name'],parameters=tool['function']['arguments'])
                if result:
                   messages.append({
                       "role":"tool",
                       "content":str(result),
                       "name":tool['function']['name']
                   })

            
        

