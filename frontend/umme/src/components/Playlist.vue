<template>
  <div class="container-fluid playlist bgDark rounded-5 p-3">
    <h5>Playlist</h5>
    <ol class="ps-2">
      <li v-for="item, index in playlistItems" class="d-flex align-items-center my-3 overflow-x-hidden" @click.prevent="evokeTrack(item.track)">
        <span class="mx-2">{{ ++index }}</span>
        <img :src="item.track.image" class="playlist-images ">
        <div class="d-flex flex-column mx-2 overflow-x-hidden">
          <p class="trackName overflow-x-hidden">{{ item.track.name }}</p>
          <p class="artistName overflow-x-hidden">{{ item.track.artists.map(artist => artist.name).join(', ') }}</p>
        </div>
      </li>
    </ol>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useToolStore } from '@/stores/tools'
import { defineEmits } from 'vue'

const tool = useToolStore()

const playlistItems = computed(() => {
  return tool.playlist
})

const emit = defineEmits(
  [
    'evokeTrack',
  ]
)

const evokeTrack = (track) => {
  emit('evokeTrack', track)
}

</script>

<style scoped>
.playlist {
  height: 100%;
}
.playlist-images {
  width: 3vh;
  height: 3vh;
}
p {
  margin: 0;
}
.trackName {
  font-size: 1.5vh;
}
.artistName {
  font-size: 1vh;
}
li:hover {
  background: #3a3a3a;
  cursor: pointer;
  transition: .2s linear;
}
</style>