import { defineStore } from 'pinia'
import api from '@/api/axios'
import { ref } from 'vue'

export const useThreadStore = defineStore('thread', () => {
  const threadItems = ref([])

  const uploadThread = async (payload) => {
    const { content, track_id } = payload
    await api.post('/threads/create/', {
      track_id,
      content,
    })
  }

  const getThreads = async (payload) => {
    const { filter } = payload
    try {
      const response = await api.get('/threads/get_threads/', {
        params: { filter },
      })
      threadItems.value = response.data
      return response.data
    } catch (error) {
      console.error(error)
    }
  }

  return {
    threadItems,

    uploadThread,
    getThreads,
  }
})
