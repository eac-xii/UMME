import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/api/axios'

export const useThreadStore = defineStore('thread', () => {
  /* ---------- state ---------- */

  const threadItems = ref([])
  const ragThreads = ref([])
  const isAIMode = ref(false)

  /* ---------- actions ---------- */

  const uploadThread = payload => {
    const { content, track_id } = payload

    return api.post('/threads/create/', {
      track_id,
      content,
    })
  }

  const getThreads = async payload => {
    const { filter } = payload

    try {
      const response = await api.get('/threads/get_threads/', {
        params: { filter },
      })

      threadItems.value = response.data
      return response.data
    } catch (error) {
      console.error('getThreads error:', error)
    }
  }

  const getThread = async threadId => {
    try {
      const response = await api.get(
        `/threads/get_thread/${threadId}/`
      )
      return response.data
    } catch (error) {
      console.error(error)
    }
  }

  const getUserThreads = async payload => {
    const { userId } = payload

    const response = await api.get('/threads/get_user_threads/', {
      params: { userId },
    })

    return response.data
  }

  const runRag = async payload => {
    isAIMode.value = true

    const response = await api.post('/rag/query/', payload)
    ragThreads.value = response.data.threads

    console.log('RAG response:', response.data)
    return response.data
  }

  const getAudiofeatures = async payload => {
    const { track_id } = payload

    const response = await api.get(
      `/musics/get_audiofeatures/${track_id}/`
    )
    return response.data
  }

  /* ---------- expose ---------- */

  return {
    // state
    threadItems,
    ragThreads,
    isAIMode,

    // actions
    uploadThread,
    getThreads,
    getThread,
    getUserThreads,
    runRag,
    getAudiofeatures,
  }
})
