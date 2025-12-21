<template>
  <div class="user-card py-3">
    <div class="userimg"></div>
    <div class="userinfo px-3">
      <div class="card-item">
        <p id="name">{{ user.name }}</p>
      </div>
      <div class="card-item">
        <p id="type">{{ user.type }}</p>
      </div>
      <div class="card-item" id="usersummary">
        <div id="followers">
          <i class="bi bi-person"></i> {{ user.followers }} 
        </div>
        <div id="songs" class="mx-2">
          <i class="bi bi-music-note-list"></i> {{ user.songs }}
        </div>
    </div>
    </div>

  </div>
</template>

<script setup>
const props = defineProps({
  'user' : Object,
})
</script>

<style scoped>
p {
  padding: 0;
  margin: 0;
}

.user-card {
  display: flex;
  align-items: center;
  border-radius: 1rem;
  background-color: #121212;
  color: #eee;
  overflow: hidden;
}

.userimg {
  width: 2.5em;
  min-width: 2rem;
  /* 가로세로비율고정 */
  aspect-ratio: 1;
  background-color: aliceblue;
  border-radius: 50%;
}

.userinfo {
  display: flex;
  flex-direction: column;
}

.card-item {
  /* 줄바꿈 방지 */
  white-space: nowrap;
  overflow: hidden;
}

/* clamp(min, val, max) */
#name {
  font-size: clamp(0.8rem, 1.2vw, 1rem);
}
#type {
  font-size: clamp(0.65rem, 1vw, 0.75rem);
}
#usersummary {
  display: flex;
  font-size: clamp(0.65rem, 1vw, 0.75rem);
}

div > i{
  margin-right: 5px;
}
</style>