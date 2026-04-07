from retriever import Retriever
import ollama # for chat model, can be changed
from langsmith import traceable

retriever = Retriever()


def build_prompt(query: str, context: str, phone_model: str):
    return f"""
You are a helpful smartphone assistant.

Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know."

Phone model: {phone_model}

Context:
{context}

Question:
{query}

Answer:
"""

@traceable(name="generate_answer")
def generate_answer(query: str, phone_model: str):
    docs = retriever.retrieve(query, phone_model)

    if not docs:
        return "I couldn't find relevant information in the manual."

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = build_prompt(query, context, phone_model)

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[{"role": "user", "content": prompt}]
    )
    #print("FETCHED context:\n", context, "\n") #for debug
    return response.message.content
