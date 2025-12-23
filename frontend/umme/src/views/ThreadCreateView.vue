<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-5">
        <Playlist @evoke-track="getTrack"/>
      </div>
      <div class="col-7">
        <ThreadCreateCard :track="trackDetail"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import Playlist from '@/components/Playlist.vue'
import ThreadCreateCard from '@/components/Thread/ThreadCreateCard.vue'
import { ref } from 'vue'

const trackDetail = ref(null)

const getTrack = (track) => {
  trackDetail.value = track
  console.log(track)
}

</script>

<style scoped>
</style>