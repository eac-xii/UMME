<template>
  <div class="container-fluid playlist ps-4">
    <h5>Playlist</h5>
    <ol class="ps-2">
      <li v-for="item, index in playlistItems" class="d-flex align-items-center my-3 overflow-x-hidden">
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

const tool = useToolStore()

const playlistItems = computed(() => tool.playlist)

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
</style>