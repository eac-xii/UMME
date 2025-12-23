<template>
  <div class="container-fluid px-4">
    <div class="row g-0">
      <section class="col-10 threadlist px-3">
        <ThreadList />
      </section>
      <section class="col-2 recommendation">
        <UserList />
      </section>
    </div>
  </div>
</template>

<script setup>
import ThreadList from '@/components/home/ThreadList.vue';
import UserList from '@/components/home/UserList.vue';
</script>

<style scoped>
.threadlist {
  display: flex;
  flex-direction: column;
}
</style>
