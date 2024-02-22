from langchain_community.llms import Ollama

llm = Ollama(model="phi:2.7b-chat-v2-q4_0")

response = llm.invoke("Tell me a joke")
print(response)
