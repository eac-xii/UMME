<template>
  <div class="thread-grid-wrapper">
    <div class="thread-grid">
      <ThreadItem v-for="thread in threads" :key="thread.title" :thread="thread" class="grid-item" />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import ThreadItem from './ThreadItem.vue'
import { useThreadStore } from '@/stores/threads';

const thread = useThreadStore()
const threads = ref([])

onMounted(async () => {
  const data = await thread.getThreads({filter:'all'})
  threads.value = data
})
</script>

<style scoped>
.thread-grid-wrapper {
  height: 70%;
  overflow-y: auto;
  padding: 1rem;
  background-color: #121212;
  border-radius: 1rem;
  box-sizing: border-box;
}

.thread-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.grid-item {
  background-color: #1e1e1e;
  border-radius: 0.5rem;
  aspect-ratio: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #aaa;
  padding: 0.5rem;
  box-sizing: border-box;
}

@media (max-width: 992px) {
  .thread-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 576px) {
  .thread-grid {
    grid-template-columns: 1fr;
  }
}

.thread-grid-wrapper::-webkit-scrollbar {
  width: 0.8rem;
}

.thread-grid-wrapper::-webkit-scrollbar-track {
  background: #1e1e1e;
  border-radius: 0.3rem;
}

.thread-grid-wrapper::-webkit-scrollbar-thumb {
  background-color: #aaa;
  border-radius: 0.3rem;
  border: 2px solid #1e1e1e;
}

.thread-grid-wrapper::-webkit-scrollbar-thumb:hover {
  background-color: #868686;
}
</style>
