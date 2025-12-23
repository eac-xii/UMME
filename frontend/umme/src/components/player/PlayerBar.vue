<template>
    <div class="row w-100">
        <PlayerInfo class="col-3" :track="currentTrack" />
        <div class="col-6">
            <PlayerControls :paused="paused" @toggle="emit('togglePlay')" @prev="emit('prev')" @next="emit('next')" />
            <PlayerProgress :position="position" :duration="duration" @seek="emit('seek', $event)" />
        </div>
        <PlayerVolume class="col-3" :volume="Number(volume)" @change="emit('setVolume', $event)" />
    </div>
</template>

<script setup>
import { computed } from 'vue'
import PlayerControls from './PlayerControls.vue'
import PlayerInfo from './PlayerInfo.vue'
import PlayerProgress from './PlayerProgress.vue'
import PlayerVolume from './PlayerVolume.vue'

const props = defineProps({
    playbackState: Object,
    paused: Boolean,
    volume: Number,
})

const emit = defineEmits([
    'togglePlay',
    'prev',
    'next',
    'seek',
    'setVolume',
])

const currentTrack = computed(() =>
    props.playbackState?.track_window?.current_track
)

const position = computed(() =>
    (props.playbackState?.position ?? 0) / 1000
)

const duration = computed(() =>
    (currentTrack.value?.duration_ms ?? 0) / 1000
)
</script>
