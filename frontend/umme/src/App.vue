<template>
  <div class="layout d-flex">
    <aside :class="['sidebar', { collapsed }]">
      <div class="nav-brand" @click="collapsed = !collapsed">
        UMME
      </div>

      <ul class="nav nav-pills flex-column">
        <li class="nav-item">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'home' }">
            Home
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'thread' }">
            Thread
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'messenger' }">
            Messenger
          </RouterLink>
        </li>
      </ul>
    </aside>
    <main class="flex-grow-1">
      <header class="top-header"></header>
      <RouterView />
    </main>
  </div>

  <div class="SDK position-fixed bottom-0 start-0">
  </div>

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { ref } from 'vue'
const collapsed = ref(false)

</script>

<style scoped>
.layout {
  height: 89.35vh;
}

.sidebar {
  width: 240px;
  background-color: #121212;
  flex-shrink: 0;
  border-top-right-radius: 30px;
  border-bottom-right-radius: 30px;
  overflow: hidden;
}

.sidebar.collapsed {
  width: 120px;
}

main {
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  background-color: #aaa3a3;
}

.top-header {
  width: auto;
  height: 11.85vh;
  background-color: #121212;
}

.SDK {
  width: 100vw;
  height: 10.65vh;
  background-color: #121212;
}

/* 기본 nav-link */
.nav-pills .nav-link {
  color: #b3b3b3;
  /* 기본 텍스트 */
  background-color: #121212;
  /* 기본 배경 */
  border-radius: 0px;
}

/* hover */
.nav-pills .nav-link:hover {
  background-color: #1e1e1e;
  color: #ffffff;
}

/* active */
.nav-pills .nav-link.active {
  background-color: #2a2a2a;
  color: #ffffff;
}

.nav-brand {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #EEEEEE;
  font-weight: 450;
  font-size: large;
  background-color: #121212;
}
</style>
