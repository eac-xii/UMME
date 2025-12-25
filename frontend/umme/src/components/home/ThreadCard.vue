<template>
  <div class="thread-card d-flex" @click="threadDetail">
    <div class="song-info d-flex flex-column align-items-center mx-4">
      <img :src="threadInfo?.track?.image" class="album-cover" alt="Album Cover">
      <div class="track-meta w-100 px-2 text-start">
        <p class="track-title my-3">{{ threadInfo?.track?.name }}</p>
        <p class="track-artist">{{ tool.formatArtists(threadInfo?.track?.artists) }}</p>
      </div>
    </div>

    <div class="thread-body flex-grow-1 px-3 d-flex flex-column">
      <div class="user-header d-flex align-items-center my-2">
        <RouterLink v-if="threadInfo" :to="{ name: 'profile', params: { id: threadInfo?.user?.pk }}"
        class="profile-icon d-flex justify-content-center align-items-center rounded-circle me-3"
        @click.stop
        >
        <UserImage :imageUrl="user?.image"/>
        </RouterLink>
        <div class="user-meta d-flex flex-row justify-content-between w-100">
          <div>
            <p class="username">{{ threadInfo?.user?.last_name }} {{ threadInfo?.user?.first_name }}</p>
            <p class="elapsed-date">{{ tool.getElapsedTime(threadInfo?.updated_at) }}</p>
          </div>
          <div class="ms-auto">
            <p><i :class="{'bi bi-heart-fill': isLiked, 'bi bi-heart': !isLiked}" @click.stop="like_thread"></i> {{ threadInfo?.like_threads?.length }}</p>
          </div>
        </div>
      </div>
      <hr class="my-2 border-secondary">
      <p class="content-text text-break my-3">{{ threadInfo?.content }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'
import { useToolStore } from '@/stores/tools'
import { useThreadStore } from '@/stores/threads'
import UserImage from '../UserImage.vue'

const account = useAccountStore()
const tool = useToolStore()
const threadStore = useThreadStore()

import { useRouter } from 'vue-router'
const router = useRouter()
const props = defineProps({
  threadId: Number,
})

const threadInfo = ref(null)
const user = ref(null)

const isLiked = computed(() => 
  threadInfo.value?.like_threads?.some(user => user.id === account.user?.pk)
)

const like_thread = async () => {
  if (!account.isAuthenticated) {
    window.alert("Login required.")
    router.push({ name: 'login'})
    return
  }
  await account.like_thread(props.threadId)
  threadInfo.value = await threadStore.getThread(props.threadId)
}

const loading = ref(true)
const error = ref(false)
watch(
  () => props.threadId,
  async () => {
    try {
      threadInfo.value = await threadStore.getThread(props.threadId)
      console.log(threadInfo.value)
    } catch {
      error.value = true
    } finally {
      loading.value = false
    }
  },
  { immediate: true }
)

const fetchThread = async () => {
  threadInfo.value = await threadStore.getThread(props.threadId)
}

onMounted(async () => {
  await fetchThread()
  user.value = await account.getProfile(threadInfo.value?.user?.pk)
})

const threadDetail = () => {
  router.push({
    name: 'thread-detail',
    params: { id: props.threadId }
  })
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
  width: 50px;
  height: 50px;
}

.username { font-size: 1rem; color: #fff; }
.elapsed-date { font-size: 0.8rem; color: #8c8c8c; }

.content-text {
  font-size: 0.95rem;
  color: #ccc;
  overflow-y: auto;
}
</style>