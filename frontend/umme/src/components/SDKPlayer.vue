<template>
    <div class="container-fluid d-flex justify-content-around">
        <div class="d-flex">
            <img id="albumImage" :src="albumImageURL" :class="{ 'placeholder': !albumImageURL }">
            <div class="d-flex flex-column justify-content-center flex-grow-1 mx-2">
                <h5 :class="{ 'placeholder': !trackName }">{{ trackName }}</h5>
                <p :class="{ 'placeholder': !artistsName }">{{ artistsName }}</p>
            </div>
        </div>
        <div class="d-flex flex-grow-1 flex-column justify-content-center">
            <div class="d-flex justify-content-center">
                <button id="previousTrack" @click.prevent="control.player.previousTrack()" class="btn">
                    <i class="bi bi-chevron-bar-left"></i>
                </button>
                <button id="togglePlay" @click.prevent="togglePlay" class="btn">
                    <i :class="{bi: true, 'bi-play': control.paused, 'bi-pause': !control.paused}"></i>
                </button>
                <button id="nextTrack" @click.prevent="control.player.nextTrack()" class="btn">
                    <i class="bi bi-chevron-bar-right"></i>
                </button>
            </div>
            <div class="d-flex justify-content-around align-items-center">
                <span id="current-time">{{ currentPositionMinute }}:{{ currentPositionSecond }}</span>
                <input type="range" id="progress-bar" class="w-75" min="0" :max="trackDuration" step="any"
                    v-model="currentPosition" @mouseup="seek" :style="{background: `linear-gradient(to right, #e0e0e0 0%, #e0e0e0 ${currentPosition / trackDuration * 100}%, #404040 ${currentPosition / trackDuration * 100}%, #404040 100%)`}">
                <span id="duration">{{ trackMinute }}:{{ trackSecond }}</span>
            </div>
        </div>
        <div class="d-flex justify-content-end align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="16px" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
            </svg>
            <input type="range" id="volume-bar" class="mx-1" value="50" v-model="volume" @input="setVolume" :style="{background: `linear-gradient(to right, #e0e0e0 0%, #e0e0e0 ${volume}%, #404040 ${volume}%, #404040 100%)`}">
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useAccountStore } from '@/stores/accounts'
import { useControlStore } from '@/stores/controls'

const account = useAccountStore()
const control = useControlStore()

const albumImageURL = ref('')
const trackName = ref('')
const artistsName = ref('')

const volume = ref(50)

let progressTimer = null
const currentPosition = ref(0)
const trackDuration = ref(0)

const currentPositionMinute = ref(0)
const currentPositionSecond = ref(0)
const trackMinute = ref(0)
const trackSecond = ref(0)

watch(
    [() => account.user?.is_spotify, () => control.sdkReady],
    async ([isSpotify, isReady]) => {
        if (!isSpotify || !isReady || control.player) return

        control.player = new Spotify.Player({
            name: 'UMME Player',
            getOAuthToken: async callback => {
                const response = await control.getPlaybackToken()
                callback(response.data.access_token)
            },
            volume: 0.5,
        })

        control.player.addListener('ready', async ({ device_id }) => {
            await control.transferPlayback(device_id)
        })

        control.player.addListener('not_ready', ({ device_id }) => {
            console.log('Device ID has gone offline', device_id)
        })

        control.player.addListener('initialization_error', ({ message }) => {
            console.error(message)
        })

        control.player.addListener('authentication_error', ({ message }) => {
            console.error(message)
        })

        control.player.addListener('account_error', ({ message }) => {
            console.error(message)
        })

        control.player.addListener('player_state_changed', state => {
            control.paused = state.paused
            if (!state) return

            const current_track = state.track_window.current_track

            if (progressTimer) {
                clearInterval(progressTimer)
                progressTimer = null
            }
            currentPosition.value = state.position / 1000
            trackDuration.value = current_track.duration_ms / 1000

            albumImageURL.value = current_track.album.images[0]?.url
            trackName.value = current_track.name
            artistsName.value = current_track.artists.map(artist => artist.name).join(' ')

            updateTimeUI()

            if (!state.paused) {
                progressTimer = setInterval(() => {
                    currentPosition.value += 0.01
                    if (currentPosition.value >= trackDuration.value) {
                        clearInterval(progressTimer)
                    }
                    updateTimeUI()
                }, 10)
            }
        })

        control.player.connect()
    },
    { immediate: true }
)

const updateTimeUI = () => {
    currentPositionMinute.value = Math.floor(currentPosition.value / 60)
    currentPositionSecond.value = Math.floor(currentPosition.value % 60)
    trackMinute.value = Math.floor(trackDuration.value / 60)
    trackSecond.value = Math.floor(trackDuration.value % 60)
}
const togglePlay = () => {
    control.player.togglePlay()
}

const setVolume = () => {
    control.player.setVolume(volume.value / 100)
}

const seek = () => {
    control.player.seek(currentPosition.value * 1000)
}
</script>

<style scoped>
#albumImage {
    width: 8.65vh;
    margin: 1vh;
    border-radius: 1vh;
    box-shadow: 1px 1px 3px black;
}
#previousTrack, #nextTrack > i {
    font-size: 1.5vh;
}
#togglePlay > i {
    font-size: 2.5vh;
}

:root {
    --box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

input[type=range] {
    appearance: none;
    background: linear-gradient(to right, #404040 0%, #404040 0%, white 0%, white 100%);
    opacity: 0.9;
    border-radius: 1vw;
    height: .5vh;
    box-shadow: var(--box-shdow);
    outline: none;
    cursor: pointer;
}

input[type=range]::-webkit-slider-thumb {
    appearance: none;
    border-radius: 1vw;
    width: .75vh;
    height: .75vh;
    background-color: white;
    box-shadow: var(--box-shdow);
    cursor: pointer;
    border: 1px solid #e0e0e0;
}

input[type=range]::-webkit-slider-thumb:hover {
    transform: scale(1.1);
}
</style>