from django.core.management.base import BaseCommand
from rag.ingestion.loader import load_documents
from rag.ingestion.splitter import split_documents
from rag.ingestion.indexer import create_vector_db, collection

class Command(BaseCommand):
    help = "Build RAG index and populate vector DB"

    def handle(self, *args, **options):
        # 문서 로드
        docs = load_documents()

        # 문서 청킹
        chunks = split_documents(docs)

        # 벡터 DB에 문서 추가
        create_vector_db(chunks, collection)

        # 확인 메시지 출력
        self.stdout.write(f"Loaded docs: {len(docs)}")
        self.stdout.write(f"Chunks created: {len(chunks)}")
