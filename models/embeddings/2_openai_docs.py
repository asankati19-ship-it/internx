from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

em = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

docs = [
    "Paris, France — on the Champ de Mars in the 7th arrondissement, near the Seine.",
    "The Eiffel Tower is in Paris, France."
]

result = em.embed_documents(docs)

print(result)