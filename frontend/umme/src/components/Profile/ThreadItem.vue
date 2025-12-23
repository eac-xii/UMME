<template>
  <div class="card text-bg-dark">
  <img src="..." class="card-img" alt="...">
  <div class="card-img-overlay">
    <h5 class="card-title">{{thread.title}}</h5>
    <p class="card-text"></p>
    <p class="card-text"><small></small></p>
  </div>
</div>
</template>

<script setup>
const props = defineProps({
  thread : Object,
})
</script>

<style scoped>
.card {
  overflow: hidden;
}
</style>