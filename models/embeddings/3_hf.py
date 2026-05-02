from langchain_huggingface import HuggingFaceEmbeddings

em = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

text = "Where is the Eiffel Tower?"

result = em.embed_query(text)

print(result)

