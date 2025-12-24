<template>
    <div class="player-progress w-100">
        <div class="progress-box d-flex align-items-center">
            <input type="range" min="0" :max="duration" step="0.1" :value="localPosition" @input="onInput"
                @change="onSeek" class="progress-bar" :style="progressStyle" />
        </div>
        <div class="time d-flex justify-content-between">
            <span>{{ currentTime }}</span>
            <span>{{ totalTime }}</span>
        </div>
    </div>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { useControlStore } from '@/stores/controls'
import { useToolStore } from '@/stores/tools'

const control = useControlStore()
const tool = useToolStore()

const localPosition = ref(control.position / 1000)
const isDragging = ref(false)

const duration = computed(() => {

    const ms = control.playbackState?.duration || 0
    return ms / 1000
})

watch(() => control.position, (newMs) => {
    if (!isDragging.value) {
        localPosition.value = newMs / 1000
    }
})

const onInput = (e) => {
    isDragging.value = true
    localPosition.value = Number(e.target.value)
}

const onSeek = () => {
    isDragging.value = false
    control.seek(localPosition.value * 1000)
}

const progressStyle = computed(() => {
    const percent = (localPosition.value / duration.value) * 100 || 0
    return {
        background: `linear-gradient(to right, rgba(192, 192, 192, 0.9) 0%, rgba(192, 192, 192, 0.9) ${percent}%, rgba(32, 32, 32, 0.5) ${percent}%, rgba(32, 32, 32, 0.5) 100%)`
    }
})

const currentTime = computed(() => tool.formatTime(localPosition.value))
const totalTime = computed(() => tool.formatTime(duration.value))
</script>

<style scoped>
.player-progress {
    padding: 0.5rem 0;
}

.progress-bar {
    appearance: none;
    width: 100%;
    height: 4px;
    border-radius: 4px;
    background: rgba(32, 32, 32, 0.5);
    cursor: pointer;
    outline: none;
}

.progress-bar::-webkit-slider-thumb {
    appearance: none;
    width: 8px;
    height: 8px;
    border-radius: 8px;
    background: rgba(240, 240, 240, 0.9);
    transition: transform 0.2s ease;
    overflow: visible;
}

.progress-bar::-webkit-slider-thumb:hover {
    transform: scale(1.2);
}

.time {
    font-size: 0.75rem;
    color: #aaa;
    margin-top: 4px;
    font-variant-numeric: tabular-nums;
}
</style>