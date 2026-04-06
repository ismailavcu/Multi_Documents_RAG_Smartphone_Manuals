from langchain_community.vectorstores import FAISS
from embedder import local_embeddings
from ingest import DB_PATH

class Retriever:
    def __init__(self):
        self.db = FAISS.load_local(
            DB_PATH,
            local_embeddings,
            allow_dangerous_deserialization=True
        )

    def retrieve(self, query: str, phone_model: str = None, k: int = 4):
        """
        Retrieve relevant documents.
        If phone_model is provided -> filter results.
        """

        # Step 1: Retrieve more docs than needed
        docs = self.db.similarity_search(query, k=10)

        # Step 2: Filter by phone_model if provided
        if phone_model:
            docs = [
                doc for doc in docs
                if doc.metadata.get("phone_model") == phone_model
            ]

        # Step 3: Return top-k
        return docs[:k]