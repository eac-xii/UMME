<template>
  <h5 class="px-4 PL-title">Playlist</h5>
  <div class="container-fluid playlist bgDark rounded-5 p-3">
    <ol class="ps-2 list-unstyled">
      <li v-for="(item, index) in playlistItems" :key="index"
        class="d-flex align-items-center my-3 p-2 rounded list-item" @click.prevent="evokeTrack(index, item.track)"
        @mouseenter="checkAllScroll($event, index)" @mouseleave="resetScroll(index)"
        :class="{'active': index === control.currentTrackIdx}">
        <span class="mx-2 index-num">{{ index + 1 }}</span>
        <img :src="item.track.image" class="playlist-images rounded flex-shrink-0">
        <div class="track-meta mx-2 flex-grow-1 overflow-hidden">
          <div class="marquee-container title-container">
            <div :class="['marquee-content', { 'scroll': scrollStates[index]?.title }]">
              <span class="marquee-text">{{ item.track.name }}</span>
              <span v-if="scrollStates[index]?.title" class="marquee-text">{{ item.track.name }}</span>
            </div>
          </div>
          <div class="marquee-container sub artist-container">
            <div :class="['marquee-content', { 'scroll': scrollStates[index]?.artist }]">
              <span class="marquee-text">{{item.track.artists.map(a => a.name).join(', ')}}</span>
              <span v-if="scrollStates[index]?.artist" class="marquee-text">{{item.track.artists.map(a =>
                a.name).join(', ')}}</span>
            </div>
          </div>
        </div>
      </li>
    </ol>
  </div>
</template>

<script setup>
import { computed, reactive } from 'vue'
import { useToolStore } from '@/stores/tools'
import { useControlStore } from '@/stores/controls'

const tool = useToolStore()
const control = useControlStore()
const emit = defineEmits(['evokeTrack'])

const playlistItems = computed(() => tool.playlist)

const scrollStates = reactive({})

const evokeTrack = (idx, track) => {
  emit('evokeTrack', idx, track)
}

const checkAllScroll = (event, index) => {
  if (!scrollStates[index]) {
    scrollStates[index] = { title: false, artist: false }
  }

  const listItem = event.currentTarget

  const titleContainer = listItem.querySelector('.title-container')
  const titleText = titleContainer.querySelector('.marquee-text')
  if (titleText.offsetWidth > titleContainer.clientWidth) {
    scrollStates[index].title = true
  }

  const artistContainer = listItem.querySelector('.artist-container')
  const artistText = artistContainer.querySelector('.marquee-text')
  if (artistText.offsetWidth > artistContainer.clientWidth) {
    scrollStates[index].artist = true
  }
}

const resetScroll = (index) => {
  if (scrollStates[index]) {
    scrollStates[index].title = false
    scrollStates[index].artist = false
  }
}
</script>

<style scoped>
 .PL-title {
  color: white;
 }
.playlist {
  height: 60vh;
  color: white;
  overflow-y: scroll;
}

.playlist::-webkit-scrollbar{
  width: 0.6vw;      /* 세로 스크롤 */
  height: 0.6vw;     /* 가로 스크롤 */
  background-color: rgba(64, 64, 64, 0.8);
  border-radius: 1vh;
}

.playlist::-webkit-scrollbar-thumb{
  background-color: rgba(128, 128, 128, 0.8);
  border-radius: 1vh;
}

.list-item {
  transition: background 0.2s linear;
}

.list-item:hover {
  background: rgba(255, 255, 255, 0.1);
  cursor: pointer;
}

.active {
  background: rgba(64, 64, 64, 0.5);
}

.playlist-images {
  width: 4vh;
  height: 4vh;
  object-fit: cover;
}

.index-num {
  min-width: 25px;
  color: #888;
  font-size: 0.9rem;
}

.track-meta {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.marquee-container {
  width: 100%;
  overflow: hidden;
  white-space: nowrap;
}

.marquee-content {
  display: inline-flex;
  gap: 30px;
  will-change: transform;
}

.marquee-text {
  display: inline-block;
  font-size: 1.5vh;
}

.sub .marquee-text {
  font-size: 1.1vh;
  color: #aaa;
}

.scroll {
  animation: marquee-animation 10s linear infinite;
}

@keyframes marquee-animation {
  0% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(calc(-50% - 15px));
  }
}
</style>