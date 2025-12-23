from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.config.settings import CHUNK_SIZE, CHUNK_OVERLAP

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    results = []
    for doc in docs:
        chunks = splitter.split_text(doc["text"])
        for chunk in chunks:
            results.append({
                "text": chunk,
                "metadata": doc["metadata"],
            })

    return results
