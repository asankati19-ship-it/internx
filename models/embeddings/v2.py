from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# load model
em = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# documents
user_docs = [
    "The Taj Mahal is in Agra, India.",
    "The Eiffel Tower is in Paris, France.",
    "The Colosseum is in Rome, Italy."
]

# query
user_query = "Where is the Eiffel Tower?"

# embeddings
user_docs_embedding = em.embed_documents(user_docs)
user_query_embedding = em.embed_query(user_query)

# similarity
results = cosine_similarity([user_query_embedding], user_docs_embedding)

# best match
best_index = results[0].argmax()
best_score = results[0][best_index]
best_answer = user_docs[best_index]

# formatted output
print("-----START-----")
print(f"Question: {user_query}")
print(f"Answer: {best_answer}")
print(f"Confidence: {best_score}")
print("-----END-----")