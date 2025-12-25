<template>
  <div class="container-fluid px-4">
    <div class="row g-0">
      <section class="col-12 threadlist px-3">
        <ThreadList />
      </section>
    </div>
  </div>
</template>

<script setup>
import ThreadList from '@/components/home/ThreadList.vue';
</script>

<style scoped>
.threadlist {
  display: flex;
  flex-direction: column;
}
</style>
