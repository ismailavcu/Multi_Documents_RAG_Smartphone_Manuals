import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from embedder import local_embeddings

DATA_PATH = "data"
DB_PATH = "vectordb"


PDF_MAP = {
    "GALAXY-NOTE20-MANUAL-ENGLISH.pdf": "note20",
    "GALAXY-Z-FOLD7-USER-GUIDE.pdf": "z fold7",
    "S23-FE-USER-GUIDE.pdf": "s23 fe",
    "S26-ULTRA-MANUAL-ENGLISH.pdf": "s26 ultra",
}


def load_documents():
    documents = []

    for file, model_name in PDF_MAP.items():
        loader = PyPDFLoader(os.path.join(DATA_PATH, file))
        pages = loader.load()

        for page in pages:
            page.metadata["phone_model"] = model_name

        documents.extend(pages)

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)


def build_vector_db(chunks):

    db = FAISS.from_documents(
        documents=chunks,
        embedding=local_embeddings
    )

    db.save_local(DB_PATH)


if __name__ == "__main__":
    
    docs = load_documents()
    chunks = split_documents(docs)

    #print("len of chunks: ", len(chunks)) #chunks are Document type
    #for chunk in chunks[:2]:
    #    print("type: ", type(chunk))
    #    print("Chunk:\n", chunk)
    
    print("\n###############\nbuild_vector_db\n")
    build_vector_db(chunks)

    print("Multi-document FAISS index created.")
    






# LOAD FAISS VECTORSTORE AND PERFORM ASK QUESTIONS # for test purpose
"""    # Perform similarity search - finds semantically similar content
loaded_vectorstore = FAISS.load_local(
    DB_PATH,
    local_embeddings,
    allow_dangerous_deserialization=True  # Required for loading pickled data
)

query = "How to unfold z fold7?"
results = loaded_vectorstore.similarity_search(query, k=3)

print("type results: ", type(results))
print("results: \n", results)


print("\n######################\nTop 3 similar documents:")
for i, doc in enumerate(results, 1):
    print(f"\n{i}. Source: {doc.metadata['source']}")
    print(f"   Phone Model: {doc.metadata['phone_model']}")
    print(f"   Content: {doc.page_content[:100]}...")"""
