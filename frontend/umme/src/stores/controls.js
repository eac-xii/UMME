import { defineStore } from 'pinia'
import api from '@/api/axios'

export const useControlStore = defineStore('control', {
    state: () => ({

    }),

    actions: {
        async getPlaybackToken() {
            return await api.get('/musics/spotify/playback_token/')
        },
        async transferPlayback(device_id) {
            await api.put('/musics/spotify/transfer_playback/', { device_id })
        }
    }
})