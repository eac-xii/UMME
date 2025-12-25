import { defineStore } from 'pinia'
import { ref, computed, onUnmounted } from 'vue'
import api from '@/api/axios'
import { useToolStore } from './tools'

export const useControlStore = defineStore('control', () => {
    const tool = useToolStore()

    const sdkReady = ref(false)
    const player = ref(null)
    const paused = ref(false)
    const playbackState = ref(null)
    const volume = ref(JSON.parse(localStorage.getItem('umme-volume')) ?? 50)
    const position = ref(0)
    const currentTrackIdx = ref(0)
    let progressTimer = null

    const getPlaybackToken = async () => {
        return await api.get('/musics/spotify/playback_token/')
    }

    const initPlayer = async () => {
        if (player.value || !window.Spotify) return

        player.value = new Spotify.Player({
            name: 'UMME Player',
            getOAuthToken: async cb => {
                const res = await getPlaybackToken()
                cb(res.data.access_token)
            },
            volume: Number(volume.value) / 100
        })

        player.value.addListener('ready', ({ device_id }) => {
            player.value.device_id = device_id
            if (tool.playlist.length > 0) {
                const payload = {
                    cIdx: 0,
                    spotify_id: tool.playlist[0].track.spotify_id
                }
                playTrack(payload)
            }
            setTimeout(() => {
                setVolume(volume.value)
            }, 1000)
        })

        player.value.addListener('player_state_changed', state => {
            if (!state) return
            paused.value = state.paused
            playbackState.value = state
            position.value = state.position

            if (!state.paused) {
                startTimer()
            } else {
                clearTimer()
            }
        })

        await player.value.connect()
    }

    const transferPlayback = async device_id => {
        await api.put('/musics/spotify/transfer_playback/', { device_id })
    }

    const playTrack = async payload => {
        const { cIdx, spotify_id } = payload
        await api.put('/musics/spotify/play/', {
            uris: [`spotify:track:${spotify_id}`],
            device_id: player.value?.device_id
        })
        currentTrackIdx.value = cIdx
    }

    const setSDKReady = value => {
        sdkReady.value = value
    }

    const setPaused = value => {
        paused.value = value
    }

    const clearTimer = () => {
        if (progressTimer) {
            clearInterval(progressTimer)
            progressTimer = null
        }
    }

    const startTimer = () => {
        clearTimer()
        if (paused.value) return

        progressTimer = setInterval(() => {
            position.value += 100
        }, 100)
    }

    const seek = async (ms) => {
        if (player.value) {
            await player.value.seek(ms)
            position.value = ms
        }
    }

    const previousTrack = async () => {
        if (tool.playlist.length === 0) return

        let maxIdx = tool.playlist.length - 1
        let targetIdx = currentTrackIdx.value
        if (targetIdx === 0) targetIdx = maxIdx
        else --targetIdx

        const payload = {
            cIdx: targetIdx,
            spotify_id: tool.playlist[targetIdx].track.spotify_id
        }
        playTrack(payload)
    }

    const nextTrack = async () => {
        if (tool.playlist.length === 0) return

        let maxIdx = tool.playlist.length - 1
        let targetIdx = currentTrackIdx.value
        if (targetIdx === maxIdx) targetIdx = 0
        else ++targetIdx

        const payload = {
            cIdx: targetIdx,
            spotify_id: tool.playlist[targetIdx].track.spotify_id
        }
        playTrack(payload)
    }

    onUnmounted(() => clearTimer())

    const setVolume = async value => {
        const numValue = Number(value)
        if (isNaN(numValue)) return

        volume.value = numValue
        localStorage.setItem('umme-volume', JSON.stringify(numValue))

        if (player.value && typeof player.value.setVolume === 'function') {
            try {
                await player.value.setVolume(numValue / 100)
            } catch (error) {
                console.error('Spotify 볼륨 조절 실패:', error)
            }
        }
    }

    const disconnect = () => {
        player.disconnect()
    }

    return {
        volume: computed(() => volume.value),

        sdkReady: computed(() => sdkReady.value),
        player: computed(() => player.value),
        paused: computed(() => paused.value),
        playbackState: computed(() => playbackState.value),

        position,
        currentTrackIdx,

        getPlaybackToken,
        initPlayer,
        transferPlayback,
        playTrack,
        previousTrack,
        nextTrack,
        seek,
        disconnect,

        setSDKReady,
        setPaused,
        setVolume
    }
})
