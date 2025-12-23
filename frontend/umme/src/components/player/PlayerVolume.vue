<template>
    <div class="player-volume d-flex align-items-center justify-content-end gap-2">
        <i class="bi" :class="volumeIcon"></i>
        <input type="range" min="0" max="100" step="1" :value="volume" @input="onInput" class="volume-slider"
            :style="{ background: `linear-gradient(to right, rgba(192, 192, 192, 0.9) 0%, rgba(192, 192, 192, 0.9) ${volume}%, rgba(32, 32, 32, 0.5) ${volume}%, rgba(32, 32, 32, 0.5) 100%)` }" />
    </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
    volume: { type: Number, required: true }
})

const emit = defineEmits(['change'])

const volumeIcon = computed(() => {
    if (props.volume === 0) return 'bi-volume-mute'
    if (props.volume < 40) return 'bi-volume-down'
    return 'bi-volume-up'
})

const onInput = (e) => {
    emit('change', Number(e.target.value))
}
</script>

<style scoped>
.volume-slider {
    width: 100px;
    appearance: none;
    height: 4px;
    border-radius: 4px;
    background: rgba(32, 32, 32, 0.5);
    outline: none;
}

.volume-slider::-webkit-slider-thumb {
    appearance: none;
    width: 8px;
    height: 8px;
    border-radius: 8px;
    background: rgba(240, 240, 240, 0.9);
    cursor: pointer;
    transition: transform 0.2s ease;
}

.volume-slider::-webkit-slider-thumb:hover {
    transform: scale(1.2);
}
</style>