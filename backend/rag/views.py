# rag/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rag.ingestion.indexer import search_vector_db, collection
from rag.config.settings import TOP_K
from musics.models import Track

class RagQueryView(APIView):
    def post(self, request):
        query = request.data.get("query")
        if not query:
            return Response({"error": "Query is required"}, status=400)
        
        results = search_vector_db(query, collection, TOP_K)

        threads = []
        for text, metadata in zip(results['documents'][0], results['metadatas'][0]):
            try:
                track = Track.objects.get(id=metadata["track_id"])
                threads.append({
                    "track_id": metadata["track_id"],
                    "content": text,
                    "created_at": metadata["created_at"],
                    "updated_at": metadata["updated_at"],
                    "track": {
                        "id": track.spotify_id,
                        "name": track.name,
                        "artists": [artist.name for artist in track.artists.all()],
                        "image": track.image if track.image else None
                    }
                })
            except Track.DoesNotExist:
                # 해당 track이 없으면 그냥 skip
                continue
        
        return Response({"threads": threads}, status=status.HTTP_200_OK)
