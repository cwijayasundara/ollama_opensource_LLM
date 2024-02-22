from langchain_community.llms import Ollama

llm = Ollama(model="gemma:7b-instruct")

response = llm.invoke("Tell me a joke")
print(response)
