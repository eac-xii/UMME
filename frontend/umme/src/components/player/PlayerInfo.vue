<template>
    <div class="player-info d-flex align-items-center gap-3">
        <div v-if="!track" class="album-image flex-shrink-0 placeholder-grow">
            <div class="placeholder w-100 h-100 rounded"></div>
        </div>
        <img v-else :src="albumImage" alt="album cover" class="album-image flex-shrink-0 rounded" />
        <div class="track-meta placeholder-grow">
            <div v-if="!track" class="py-1">
                <span class="placeholder col-8"></span>
            </div>
            <div v-else class="marquee">
                <div :class="['marquee-content', { scroll: needsScroll }]">
                    <span ref="textRef" class="marquee-text">{{ track?.name }}</span>
                    <span v-if="needsScroll" class="marquee-text">{{ track?.name }}</span>
                </div>
            </div>
            <div v-if="!track" class="py-1">
                <span class="placeholder col-5 bg-secondary"></span>
            </div>
            <div v-else class="marquee sub">
                <div :class="['marquee-content', { scroll: artistNeedsScroll }]">
                    <span ref="artistRef" class="marquee-text">{{ artists || '-' }}</span>
                    <span v-if="artistNeedsScroll" class="marquee-text">{{ artists }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed, ref, watch, nextTick } from 'vue'
import { useToolStore } from '@/stores/tools'

const tool = useToolStore()

const props = defineProps({
    track: { type: Object, default: null },
})

const textRef = ref(null)
const artistRef = ref(null)
const needsScroll = ref(false)
const artistNeedsScroll = ref(false)

const albumImage = computed(() => props.track?.album?.images?.[0]?.url || '')
const artists = computed(() => tool.formatArtists(props.track?.artists) || '')

const updateScrollStatus = async () => {
    await nextTick()
    await nextTick()

    if (textRef.value) {
        const container = textRef.value.closest('.marquee')
        if (container) {
            needsScroll.value = textRef.value.offsetWidth > container.clientWidth
        }
    }

    if (artistRef.value) {
        const container = artistRef.value.closest('.marquee.sub')
        if (container) {
            artistNeedsScroll.value = artistRef.value.offsetWidth > container.clientWidth
        }
    }
}

watch(() => props.track, (newTrack) => {
    if (newTrack) {
        updateScrollStatus()
    } else {
        needsScroll.value = false
        artistNeedsScroll.value = false
    }
}, { immediate: true, deep: true })
</script>

<style scoped>
.album-image {
    width: 8vh;
    height: 8vh;
    object-fit: cover;
}

.track-meta {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.marquee {
    width: 100%;
    overflow: hidden;
    position: relative;
    white-space: nowrap;
}

.marquee-content {
    display: inline-flex;
    gap: 50px;
    will-change: transform;
}

.marquee-text {
    display: inline-block;
}

.marquee:not(.sub) .marquee-content.scroll {
    animation: marquee-animation 20s linear infinite;
}

.marquee.sub .marquee-content.scroll {
    animation: marquee-animation 28s linear infinite;
}

.marquee.sub {
    font-size: 0.85rem;
    color: #aaa;
}

.player-info:hover .marquee-content {
    animation-play-state: paused;
}

@keyframes marquee-animation {
    0% {
        transform: translateX(0);
    }

    100% {
        transform: translateX(calc(-50% - 25px));
    }
}

.placeholder {
    display: inline-block;
    min-height: 1em;
    vertical-align: middle;
    cursor: wait;
}
</style>