<template>
  <div class="userlist-layout">
    <div class="userlist card px-2">
      <div class="titlebar px-4">
        <span class="title">UMME</span>
        <span><i class="bi bi-arrow-clockwise"></i></span>
      </div>
      <div class="px-4 row">
        <div v-for="user in users" :key="user.name">
          <UserCard :user="user" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import UserCard from './UserCard.vue';
const users = ref([
  { name: 'eacxii', type: '(type)', followers: 30, songs: 14 },
  { name: 'xxxez', type: '(type)', followers: 24, songs: 10 },
  { name: 'bsus_13', type: '(type)', followers: 54, songs: 42 },
  { name: 'seo_oy', type: '(type)', followers: 67, songs: 23 },
  { name: 'endkdl33', type: '(type)', followers: 43, songs: 39 },
  { name: 'kch0324', type: '(type)', followers: 13, songs: 8 },
  { name: 'nn.j.w', type: '(type)', followers: 5, songs: 5 },
])
</script>

<style scoped>
.userlist-layout{
  height: 70vh;
  margin-right: 2rem;
}

.userlist {
  margin-top: 50px;
  border-radius: 1rem;
  background-color: #121212;
  overflow: hidden;
}

.titlebar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: nowrap;
  height: 50px;
  margin-top: 0.5rem;
  color: #eee;
  overflow: hidden;
}

.title>i {
  font-size: 25px;
}
</style>