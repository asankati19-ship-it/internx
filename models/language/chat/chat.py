from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-4o")

result = cm.invoke("What is the capital of France?")

print(result.content)
