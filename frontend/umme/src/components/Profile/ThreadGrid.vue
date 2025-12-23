<template>
  <div class="thread-grid-wrapper">
    <div class="thread-grid">
      <ThreadItem
        v-for="thread in threads"
        :key="thread.title"
        :thread="thread"
        class="grid-item"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ThreadItem from './ThreadItem.vue'

const threads = ref([
  { title: 'Thread1', content: 'Content1' },
  { title: 'Thread2', content: 'Content2' },
  { title: 'Thread3', content: 'Content3' },
  { title: 'Thread4', content: 'Content4' },
  { title: 'Thread5', content: 'Content5' },
  { title: 'Thread6', content: 'Content6' },
  { title: 'Thread7', content: 'Content7' },
  { title: 'Thread8', content: 'Content8' },
  { title: 'Thread9', content: 'Content9' },
  { title: 'Thread10', content: 'Content10' },
])
</script>

<style scoped>

.thread-grid-wrapper {
  height: 70%;
  /* 스크롤 */
  overflow-y: auto;
  padding: 1rem;
  background-color: #121212;
  border-radius: 1rem;
  box-sizing: border-box;
}

/* 그리드 */
.thread-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

/* 카드 */
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

/* 반응형: 2열 */
@media (max-width: 992px) {
  .thread-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* 반응형: 1열 */
@media (max-width: 576px) {
  .thread-grid {
    grid-template-columns: 1fr;
  }
}


/* TODO : header 배경색 변경 필요 */
/* 스크롤바 전체 */
.thread-grid-wrapper::-webkit-scrollbar {
  width: 0.8rem; /* 스크롤바 두께 */
}
/* 스크롤바 트랙 (배경) */
.thread-grid-wrapper::-webkit-scrollbar-track {
  background: #1e1e1e; /* 트랙 색상 */
  border-radius: 0.3rem;
}
/* 스크롤바 막대 (드래그 가능한 부분) */
.thread-grid-wrapper::-webkit-scrollbar-thumb {
  background-color: #aaa; /* 막대 색상 */
  border-radius: 0.3rem;
  border: 2px solid #1e1e1e; /* 막대 외곽 */
}
/* 호버 시 색상 변경 */
.thread-grid-wrapper::-webkit-scrollbar-thumb:hover {
  background-color: #868686;
}
</style>

