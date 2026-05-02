from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

em = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

text = "Where is the Eiffel Tower?"

result = em.embed_query(text)

print(result)