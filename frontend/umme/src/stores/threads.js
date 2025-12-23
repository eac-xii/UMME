import { defineStore } from 'pinia'
import api from '@/api/axios'
import { ref } from 'vue'

export const useThreadStore = defineStore('thread', {
    state: () => ({
      threadItems: [],
    }),

    actions: {
      uploadThread(payload) {
        const { content, track_id } = payload
        api.post('/threads/create/', {
          track_id,
          content,
        })
      },
      async getThreads(payload) {
        const { filter } = payload
        try {
          const response = await api.get('/threads/get_threads/', { 
            params: {
              filter,
            }
           })
          this.threadItems = response.data
          console.log(response.data)
          return response.data
        } catch (error) {}
      }
    }
})