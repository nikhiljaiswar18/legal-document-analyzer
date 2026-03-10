import faiss
import numpy as np

def create_vector_store(embeddings):

    # Get vector dimension
    dimension = len(embeddings[0])

    # Create FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to index
    index.add(np.array(embeddings))

    return index