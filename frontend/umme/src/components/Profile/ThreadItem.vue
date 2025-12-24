<template>
  <div class="card text-bg-dark">
    <img :src="thread.track?.image" class="card-img" alt="...">
    <div class="card-img-overlay">
      <div class="track-info">
        <h5 class="card-title">{{ thread.track?.name }}</h5>
      </div>
      <p class="card-text"></p>
      <p class="card-text"><small></small></p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  thread: Object,
})
</script>

<style scoped>
.card {
  overflow: hidden;
}

.track-info {
  width: 100%;
  display: flex;
}


.card-title {
  font-size: 1rem;
  font-weight: 200;
  padding: 0.2rem;
  background-color: black;
}
</style>