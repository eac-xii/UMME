<template>
  <div class="px-4">
    <div class="filter">
      <button type="button" class="btn filter-item" @click.prevent="getThreads('all')">All</button>
      <button type="button" class="btn filter-item" @click.prevent="getThreads('follow')">Follow</button>
      <button type="button" class="btn filter-item" @click.prevent="getThreads('liked')">Liked</button>
      <hr class="line">
    </div>
    <div class="thread-layout">
      <div 
      class="mx-2 mb-3 p-0" 
      v-for="thread in threads" 
      :key="thread.id"
      >
        <ThreadCard :threadId="thread.id"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import ThreadCard from './ThreadCard.vue'
import { useAccountStore } from '@/stores/accounts'
import { useThreadStore } from '@/stores/threads'

const account = useAccountStore()
const thread = useThreadStore()

const threads = computed(() => {
  return thread.isAIMode
  ? thread.ragThreads
  : thread.threadItems
})

onMounted(async () => {
  if (!account.isAuthenticated) return
  await getThreads('all')
})

const getThreads = async (filter) => {
  await thread.getThreads({ filter })
}

</script>

<style scoped>
.test {
  color:white;
}
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
  font-size: 1.2vh;
  text-align: start;
  color: #aaa;
}

.filter-item:hover {
  transition: .2s ease;
  transform: scale(1.05);
  color: #eee;
}

.line {
  flex: 1;
  margin: 0 0.5rem;
}
</style>