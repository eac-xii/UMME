from threads.services import fetch_threads_for_rag

def load_documents():
    return list(fetch_threads_for_rag())