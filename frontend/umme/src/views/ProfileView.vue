<template>
  <div class="row view-container">
    <div class="col">
      <div class="row detail">
        <div class="col">
          <UserInfo :userId="userId"/>
        </div>
        <div class="col">
          <UserType :userId="userId"/>
        </div>
      </div>
      <div class="row activity">
        <div class="col">
          <ThreadGrid :userId="userId"/>
        </div>
        <div class="col">
          <Playlist :userId="userId"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import UserInfo from '@/components/Profile/UserInfo.vue'
import ThreadGrid from '@/components/Profile/ThreadGrid.vue'
import UserType from '@/components/Profile/UserType.vue'
import Playlist from '@/components/Profile/Playlist.vue'

import { useRoute } from 'vue-router'

const route = useRoute()
const userId = route.params.id
</script>

<style scoped>
.view-container {
  height: 100%;
}
.detail {
  max-height: 30vh;
}
.activity {
  max-height: 55vh;
}
</style>
