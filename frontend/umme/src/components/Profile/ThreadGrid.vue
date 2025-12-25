<template>
  <div class="thread-grid-wrapper">
    <div class="thread-grid px-4">
      <ThreadItem 
      v-for="thread in threads" 
      :key="thread.title" 
      :thread="thread" 
      class="grid-item" />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import ThreadItem from './ThreadItem.vue'
import { useThreadStore } from '@/stores/threads';

const thread = useThreadStore()
const threads = ref([])

const props = defineProps({
  userId: String
})

onMounted(async () => {
  const payload = {
    userId: props.userId
  }
  const data = await thread.getUserThreads(payload)
  threads.value = data
})
</script>

<style scoped>
.thread-grid-wrapper {
  max-height: 55vh;
  overflow-y: auto;
  padding: 1rem;
  background: #000;
  border-radius: 1rem;
  box-sizing: border-box;
}

.thread-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1vh;
}

.grid-item {
  background-color: #1e1e1e;
  aspect-ratio: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #aaa;
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
  width: .8vh;
}

.thread-grid-wrapper::-webkit-scrollbar-track {
  background: #000;
  border-radius: 3vh;
}

.thread-grid-wrapper::-webkit-scrollbar-thumb {
  background-color: #121212;
  border-radius: 0vh;
}

.thread-grid-wrapper::-webkit-scrollbar-thumb:hover {
  background-color: #404040;
}
</style>
