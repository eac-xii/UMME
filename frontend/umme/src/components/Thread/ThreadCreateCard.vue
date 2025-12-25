<template>
  <div class="createCard rounded-5 p-4 mx-4">
    <div class="row">
      <div class="col-4 p-3">
        <img :src="props.track?.image"/>
      </div>

      <div class="col-8">
        <div class="d-flex align-items-center my-3">
          <div class="profileBtn d-flex justify-content-center align-items-center rounded-circle me-3">
            {{ account.user?.last_name[0].toUpperCase() }}
          </div>
          <span>{{ account.user?.last_name }} {{ account.user?.first_name }}</span>
        </div>

        <hr class="border-secondary" />

        <div class="py-3 text-secondary">
          <p>Title <span class="mx-2">|</span> {{ props.track?.name }}</p>
          <p>Artist <span class="mx-2">|</span> {{props.track?.artists.map(a => a.name).join(', ')}}</p>
        </div>
      </div>
    </div>

    <!-- textarea -->
    <div class="row">
      <div class="col m-3">
        <textarea v-model="content" class="threadcontent rounded-4 w-100"
          placeholder="이 음악에 대한 생각을 가볍게 적어보세요…"></textarea>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <button type="button" class="btn bgGreen" @click.prevent="uploadThread">
          Upload
        </button>
      </div>
    </div>
  </div>
  <div aria-alive="polite" class="toast-container position-fixed bottom-0 end-0 p-3">
    <div ref="toastElement" class="toast" role="alert" aria-live="polite" aria-atomic="true">
      <div class="toast-header">
        <strong class="me-auto">UMME</strong>
      </div>
      <div class="toast-body">
        Thread for {{ props.track?.name }} created!
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import * as bootstrap from 'bootstrap'
import { useAccountStore } from '@/stores/accounts'
import { useThreadStore } from '@/stores/threads'
import { useRouter } from 'vue-router'

const account = useAccountStore()
const thread = useThreadStore()
const router = useRouter()

const props = defineProps({
  track: Object,
})

const content = ref('')
const toastElement = ref(null)

const uploadThread = () => {
  if (!props.track) return alert('Select track first!')
  if (!content.value) return alert('Type any content!')

  thread.uploadThread({
    content: content.value,
    track_id: props.track.spotify_id,
  })


  if (toastElement.value) {
    const toast = bootstrap.Toast.getOrCreateInstance(toastElement.value)
    toast.show()
  }

  content.value = ''
  setTimeout(() => {
    router.push({ name: 'home' })
  }, 1500)
}
</script>

<style scoped>
.createCard {
  background-color: #121212;
  width: 50rem;
  height: 100%;
}

/* image */
img {
  width: 100%;
  border-radius: 1rem;
}

/* profile */
.profileBtn {
  width: 36px;
  height: 36px;
  background-color: #1ed760;
  color: #121212;
  font-weight: 700;
}

/* ===== textarea 핵심 ===== */
.threadcontent {
  height: 30vh;
  padding: 1.5rem;
  background-color: #1b1b1b;
  color: #ddd;

  border: 1px solid #2a2a2a;
  outline: none;
  resize: none;

  font-size: 0.95rem;
  line-height: 1.6;
  box-sizing: border-box;

  transition: border 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
}

.threadcontent::placeholder {
  color: #777;
}

/* focus 상태 */
.threadcontent:focus {
  background-color: #1f1f1f;
  border-color: #1ed760;
  box-shadow: 0 0 0 2px rgba(30, 215, 96, 0.15);
}

/* 스크롤바 */
.threadcontent::-webkit-scrollbar {
  width: 6px;
}

.threadcontent::-webkit-scrollbar-thumb {
  background-color: rgba(255, 255, 255, 0.15);
  border-radius: 4px;
}

.threadcontent::-webkit-scrollbar-track {
  background-color: transparent;
}

/* 버튼 */
.bgGreen {
  background-color: #1ed760;
  color: #121212;
  font-weight: 600;
  width: 100%;
}

.bgGreen:hover {
  background-color: #1bd45a;
}

.toast-header {
  background-color: #1ed760;
  color: #121212;
}
.toast-body {
  background-color: #121212;
  color: #eee;
}
</style>
