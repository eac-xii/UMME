from threads.models import Thread

def fetch_threads_for_rag():
    return Thread.objects.values(
        "track_id",
        "content",
        "created_at",
        "updated_at",
    )
