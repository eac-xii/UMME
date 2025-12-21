<template>
  <div>
    <div class="filter">
      <div class="filter-item">All</div>
      <div class="filter-item">Follow</div>
      <hr class="line">
    </div>
    <div class="mx-2 mb-3 p-0" 
    v-for="thread in threads" 
    :key="thread.title"
    >
    <ThreadCard :thread="thread"/>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ThreadCard from './ThreadCard.vue';

const threads = ref([
  { title: 'Thread1', content: 'content1'},
  { title: 'Thread2', content: 'content2'},
  { title: 'Thread3', content: 'content3'},
])
</script>

<style scoped>
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