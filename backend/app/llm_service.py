from transformers import pipeline

# Load lightweight text generation model
generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_length=512
)

def generate_answer(question, context_chunks):

    context = " ".join(context_chunks)

    prompt = f"""
    You are a legal assistant.

    Answer the question based on the context.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    result = generator(prompt)

    return result[0]["generated_text"]