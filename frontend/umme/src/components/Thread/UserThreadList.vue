<template>
  <div class="layout">
    <div class="filter">
      <hr class="line">
    </div>
    <div class="thread-layout">
      <div 
      class="mx-2 mb-3 p-0" 
      v-for="thread in threads" 
      :key="thread.id"
      >
        <ThreadCard :thread="thread"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import ThreadCard from '@/components/home/ThreadCard.vue'
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
import { useThreadStore } from '@/stores/threads'
import api from '@/api/axios'

const thread = useThreadStore()
const route = useRoute()
const userId = route.params.id

const threads = ref([])
const user = ref(null)

onMounted(async () => {
  const payload = {
    userId: userId
  }
  const data = await thread.getUserThreads(payload)
  threads.value = data
  
})
console.log('threads:',threads)
</script>

<style scoped>
.thread-layout{
  height: 80vh;
  overflow-y: scroll;
  scrollbar-width: none;
}

.thread-layout::-webkit-scrollbar{
  display: none;
}

.filter {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  height: 50px;
  padding: 0 10px;
  
}

.filter-item {
  display: inline-flex;
  margin-right: 10px;
  font-size: x-small;
  text-align: start;
  color: #aaa;
}

.line {
  flex: 1;
  margin: 0 0.5rem;
}
</style>