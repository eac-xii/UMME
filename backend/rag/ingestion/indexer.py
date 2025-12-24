import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "umme.settings"   # ⚠️ 프로젝트 이름에 맞게
)
django.setup()

from threads.services import fetch_threads_for_rag
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer
from rag.config.settings import TOP_K


load_dotenv()
token = os.getenv('HUGGING_FACE_HUB_TOKE')

# 한국어 RoBERTa 모델 로드 (jhgan/ko-sroberta-multitask)
embedding_model = SentenceTransformer('jhgan/ko-sroberta-multitask')

client = chromadb.Client()
collection = client.create_collection(name="rag_index")

# docs = list(fetch_threads_for_rag())
# 스레드 vectorDB에 저장
def create_vector_db(docs, collection):
    for doc in docs:
        text = doc["content"]

        vector = embedding_model.encode(text)

        metadata = {
            "track_id": doc["track_id"],
            "created_at": doc["created_at"].isoformat(),
            "updated_at": doc["updated_at"].isoformat(),
        }

        collection.add(
            documents=[text],
            metadatas=[metadata],
            embeddings=[vector],
            ids=[str(doc["track_id"])]
        )

    # print("벡터db 저장완")

# create_vector_db(docs, collection)

# 질문에 맞는 문서 반환
def search_vector_db(query, collection, top_k):
    """
    주어진 쿼리에 대해 유사한 문서를 벡터 DB에서 검색합니다.
    """
    # 쿼리 벡터화
    query_vector = embedding_model.encode(query)

    # 유사 문서 검색
    results = collection.query(
        query_embeddings=[query_vector], 
        n_results=TOP_K
    )
    
    return results