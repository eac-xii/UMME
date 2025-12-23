<template>
    <div class="player-controls">
        <button class="btn" @click="$emit('prev')" aria-label="이전 곡">
            <i class="bi bi-chevron-bar-left"></i>
        </button>
        <button class="btn play-btn" @click="$emit('toggle')" :aria-label="paused ? 'play' : 'pause'">
            <i class="bi" :class="paused ? 'bi-play' : 'bi-pause'"></i>
        </button>
        <button class="btn" @click="$emit('next')" aria-label="다음 곡">
            <i class="bi bi-chevron-bar-right"></i>
        </button>
    </div>
</template>

<script setup>
defineProps({
    paused: {
        type: Boolean,
        required: true,
    },
})

defineEmits(['prev', 'next', 'toggle'])
</script>

<style scoped>
.player-controls {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1.8rem;
}

.btn {
    background: none;
    border: none;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity .2s ease;
}

.btn:hover {
    opacity: 0.7;
}

.btn:active {
    transform: scale(0.95);
}

.btn i {
    font-size: 1.5vh;
}

.play-btn i {
    font-size: 3vh;
}
</style>