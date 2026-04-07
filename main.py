# for langsmith load api key
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# load_dotenv loads: os.getenv('LANGSMITH_PROJECT'), os.getenv('LANGSMITH_API_KEY'), os.getenv('LANGSMITH_TRACING_V2')


#from langsmith import traceable
from utils import extract_phone_model
from rag import generate_answer

#@traceable(name="RAG chat") # no need here? see rag.py generate_answer function
def chat():
    print(" ###### Multi-Document RAG Assistant ###### ")
    print("Type 'exit' to quit\n")

    current_model = None

    while True:
        query = input("You: ").strip()

        if query.lower() == "exit":
            break

        # Step 1: Try to detect model from query
        detected_phone_model = extract_phone_model(query)

        if detected_phone_model:
            current_model = detected_phone_model

        # Step 2: Ask user if model not known
        if not current_model:
            print("Assistant: I'm here to answer your smartphone questions. What is your phone model? For example: s26 ultra?")
            continue

        # Step 3: Generate answer
        answer = generate_answer(query, current_model)

        print(f"\nAssistant:\n{answer}\n")


if __name__ == "__main__":
    chat()