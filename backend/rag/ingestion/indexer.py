from dotenv import load_dotenv
import os
import chromadb
from sentence_transformers import SentenceTransformer
from loader import load_documents
import uuid
from pprint import pprint
from rag.config.settings import TOP_K


load_dotenv()
token = os.getenv('HUGGING_FACE_HUB_TOKE')

# 한국어 RoBERTa 모델 로드 (jhgan/ko-sroberta-multitask)
embedding_model = SentenceTransformer('jhgan/ko-sroberta-multitask')

client = chromadb.Client()
collection = client.create_collection(name="rag_index")

docs = load_documents()
# 스레드 vectorDB에 저장
def create_vector_db(docs, collection):
    for doc in docs:
        text = doc['text']
        # 한국어 임베딩 생성
        vector = embedding_model.encode(text)
        document_id = str(uuid.uuid4())
        # 메타데이터 포함해서 벡터db에 저장
        collection.add(
            documents=[text],
            metadatas=[doc['metadata']],
            embeddings=[vector],
            ids=[document_id]
        )
    print("벡터db 저장완")
create_vector_db(docs, collection)

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
        n_results=top_k
    )
    
    return results
query = "기타에 대한 평가가 좋은 스레드 보여줘"
results = search_vector_db(query, collection, TOP_K)

pprint(results)