<template>
  <div class="thread-card d-flex" @click="threadDetail">
    <div class="song-info d-flex flex-column align-items-center mx-4">
      <img :src="thread.track?.image" class="album-cover" alt="Album Cover">
      <div class="track-meta w-100 px-2 text-start">
        <p class="track-title my-3">{{ thread.track?.name }}</p>
        <p class="track-artist">{{ thread.track?.artists.map(a => a.name).join(', ') }}</p>
      </div>
    </div>

    <div class="thread-body flex-grow-1 px-3 d-flex flex-column">
      <div class="user-header d-flex align-items-center my-2">
        <div class="profile-icon d-flex justify-content-center align-items-center rounded-circle me-3">
          {{ thread.user?.last_name?.[0].toUpperCase() }}
        </div>
        <div class="user-meta">
          <p class="username">{{ thread.user?.last_name }} {{ thread.user?.first_name }}</p>
          <p class="elapsed-date">{{ getElapsedTime(thread.updated_at) }}</p>
        </div>
      </div>
      <hr class="my-2 border-secondary">
      <p class="content-text text-break my-3">{{ thread.content }}</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const props = defineProps({
  thread: { type: Object, required: true },
})

// const user_threadlist = () => {
//   console.log('thread prop: ', props.thread)
//   router.push({
//     name: 'thread-detail',
//     params: { id: props.thread.user.pk }
//   })
// }

const threadDetail = () => {
  router.push({
    name: 'thread-detail',
    params: { id: props.thread.id }
  })
}

const getElapsedTime = (isoString) => {
  if (!isoString) return ''
  const diffMs = new Date() - new Date(isoString)
  const diffMin = Math.floor(diffMs / 60000)
  const diffHour = Math.floor(diffMin / 60)
  const diffDay = Math.floor(diffHour / 24)

  if (diffMin < 1) return 'now'
  if (diffMin < 60) return `${diffMin} minutes ago`
  if (diffHour < 24) return `${diffHour} hours ago`
  return `${diffDay} days ago`
}
</script>

<style scoped>
p { margin: 0; padding: 0; }

.thread-card {
  height: 25rem;
  border-radius: 1rem;
  background-color: #121212;
  color: #eee;
  padding: 3rem;
  gap: 2rem;
}

.song-info {
  width: 12rem;
  flex-shrink: 0;
}

.album-cover {
  width: 100%;
  aspect-ratio: 1;
  border-radius: 1rem;
  object-fit: cover;
  background-color: #333;
  margin-bottom: 0.75rem;
}

.thread-body{
  overflow: hidden;
}

.track-title, .track-artist {
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.track-title { font-size: 1rem; font-weight: 300; }
.track-artist { font-size: 0.85rem; color: #b3b3b3; }

.profile-icon {
  background-color: #1ed760;
  width: 40px;
  height: 40px;
  color: #000;
  font-weight: bold;
}

.username { font-size: 1rem; color: #fff; }
.elapsed-date { font-size: 0.8rem; color: #8c8c8c; }

.content-text {
  font-size: 0.95rem;
  color: #ccc;
  overflow-y: auto;
}
</style>