import { defineStore } from 'pinia'
import api from '@/api/axios'

export const useThreadStore = defineStore('thread', {
  state: () => ({
    threadItems: [],
    ragThreads: [],
    isAIMode: false,
  }),

  actions: {
    uploadThread(payload) {
      const { content, track_id } = payload

      return api.post('/threads/create/', {
        track_id,
        content,
      })
    },

    async getThreads(payload) {
      const { filter } = payload

      try {
        const response = await api.get('/threads/get_threads/', {
          params: { filter },
        })

        this.threadItems = response.data
        return response.data
      } catch (error) {
        console.error('getThreads error:', error)
      }
    },
    async getUserThreads(payload) {
      const { userId } = payload
      const response = await api.get('/threads/get_user_threads/', {
        params: {
          userId
        }
      })
      return response.data
    },

    async runRag(payload) {
      this.isAIMode = true
      const response = await api.post('/rag/query/', payload)
      this.ragThreads = response.data.threads
      console.log('RAG response:', response.data)
      return response.data
    },
  },
})
