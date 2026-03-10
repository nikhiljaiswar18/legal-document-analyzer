import numpy as np
from sentence_transformers import SentenceTransformer

# Load the same embedding model used earlier
model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_relevant_chunks(question, index, chunks, top_k=3):

    # Convert question into embedding
    question_embedding = model.encode([question])

    # Search FAISS index
    distances, indices = index.search(np.array(question_embedding), top_k)

    # Retrieve the relevant chunks
    results = [chunks[i] for i in indices[0]]

    return results