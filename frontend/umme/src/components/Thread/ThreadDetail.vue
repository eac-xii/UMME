<template>
  <div class="w-full h-full p-4 flex flex-col">
    <div v-if="thread">
      <!-- 스레드 제목 -->
      <h1 class="text-xl font-bold mb-2">{{ thread.title }}</h1>
      
      <!-- 작성자 정보 -->
      <div class="text-sm text-gray-500 mb-4">
        작성자: {{ thread.user.username }} | 작성일: {{ thread.created_at }}
      </div>

      <!-- 내용 -->
      <div class="text-base text-gray-800">
        {{ thread.content }}
      </div>
    </div>

    <div v-else class="text-gray-400 text-center mt-10">
      스레드를 불러오는 중...
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useThreadStore } from '@/stores/threads'
import api from '@/api/axios'
const route = useRoute()
const threadStore = useThreadStore()

const threadId = Number(route.params.threadId)
const thread = ref(null)

onMounted(async () => {
  const res = await api.get(`/threads/${route.params.threadId}/`)
  thread.value = res.data
})
</script>

<style scoped>
/* 스크롤 필요 시 */
div {
  overflow-y: auto;
}
</style>
