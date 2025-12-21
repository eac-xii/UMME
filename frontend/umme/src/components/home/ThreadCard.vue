<template>
  <div class="thread-card p-3">
    <h5>{{ thread.title }}</h5>
    <p>{{ thread.content }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  'thread' : Object,
})
</script>

<style scoped>
.thread-card {
  border-radius: 1rem;
  background-color: #121212;
  overflow: hidden;
}
</style>