from langchain_huggingface import HuggingFaceEmbeddings

em = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

user_docs=[

    "The Taj Mahal is located in Agra, India.",
    "The Eiffel Tower is located in Paris, France.",
    "The Colosseum is located in Rome, Italy."
]

user_query = "Where is the Eiffel Tower?"

user_docs_embeddings = em.embed_documents(user_docs)

user_query_embeddings = em.embed_query(user_query)

# cosine similarity

from sklearn.metrics.pairwise import cosine_similarity

results = cosine_similarity([user_query_embeddings], user_docs_embeddings)

best_match_index = results[0].argmax()

answer = user_docs[best_match_index]

print(answer)
