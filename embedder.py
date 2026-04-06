from langchain_community.embeddings import HuggingFaceEmbeddings

MODEL_NAME = "all-MiniLM-L6-v2"

local_embeddings = HuggingFaceEmbeddings(
    model_name=MODEL_NAME,  # 384 dimensions, fast
    model_kwargs={"device": "cpu"},  # Use "cuda" for GPU
    encode_kwargs={"normalize_embeddings": True}
)
    