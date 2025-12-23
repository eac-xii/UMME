import { defineStore } from 'pinia'
import api from '@/api/axios'
import { ref } from 'vue'

export const useControlStore = defineStore('control', {
    state: () => ({
        sdkReady: ref(false),
        player: ref(null),
        paused: ref(false)
    }),

    actions: {
        async getPlaybackToken() {
            return await api.get('/musics/spotify/playback_token/')
        },
        async transferPlayback(device_id) {
            await api.put('/musics/spotify/transfer_playback/', { device_id })
        },
        async playTrack(payload) {
            const { spotify_id } = payload
            await api.put('/musics/spotify/play/', {
                uris: [`spotify:track:${spotify_id}`],
                device_id: this.player.device_id
            })
        }
    }
})