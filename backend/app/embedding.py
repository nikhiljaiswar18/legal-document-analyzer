from sentence_transformers import SentenceTransformer

# Load a pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    """
    Converts text chunks into vector embeddings
    """

    embeddings = model.encode(chunks)

    return embeddings