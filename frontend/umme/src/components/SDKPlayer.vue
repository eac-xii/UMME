<template>
    <PlayerBar :playback-state="control.playbackState" :paused="control.paused" :volume="control.volume"
        @toggle-play="control.player?.togglePlay()" @seek="ms => control.seek(ms)" @set-volume="control.setVolume"
        @prev="control.previousTrack()" @next="control.nextTrack()" />
</template>

<script setup>
import { watch } from 'vue'
import { useAccountStore } from '@/stores/accounts'
import { useControlStore } from '@/stores/controls'
import PlayerBar from './player/PlayerBar.vue'

const account = useAccountStore()
const control = useControlStore()

watch(
    [() => account.user?.is_spotify, () => control.sdkReady],
    async ([isSpotify, isReady]) => {
        if (!isSpotify || !isReady || control.player) return
        await control.initPlayer()
    },
    { immediate: true }
)
</script>