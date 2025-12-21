<template>
  <div class="user-viewport d-flex">
    <aside :class="['sidebar', { collapsed }]">
      <div class="nav-brand" @click="collapsed = !collapsed">
        <PhCow :size="32" class="mx-2"/>
        <span class="mx-2">{{ collapsed ? '' : 'UMME' }}</span>
      </div>

      <ul class="nav nav-pills flex-column">
        <li class="nav-item">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'home' }">
            <PhHouse size="20" weight="regular" class="mx-3"/> 
            <span>{{ collapsed ? '' : homeText }}</span>
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'thread' }">
            <!-- <i class="bi bi-pencil-square px-3"></i> -->
            <PhNotePencil size="20" weight="regular" class="mx-3"/> 
            <span>{{ collapsed ? '' : threadText }}</span>
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'messenger' }">
            <!-- <i class="bi bi-envelope px-3"></i>  -->
            <PhMessengerLogo size="20" weight="regular" class="mx-3"/>
            {{ collapsed ? '' : messengerText }}
          </RouterLink>
        </li>
      </ul>
      <hr class="m-4">
    </aside>
    <main class="flex-grow-1">
      <header class="top d-flex align-items-center px-3">
        <div class="searchBox d-flex align-items-center">
          <i class="bi bi-search"></i>
        </div>

        <div class="profileBtn d-flex justify-content-center align-items-center ms-auto">
          <span>Y</span>
        </div>
      </header>
      <RouterView />
    </main>
  </div>

  <div class="SDK position-fixed bottom-0 start-0">
  </div>

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { ref } from 'vue'
import { PhHouse, PhNotePencil, PhMessengerLogo, PhCow } from '@phosphor-icons/vue'

const collapsed = ref(false)
const homeText = ref('Home')
const threadText = ref('Thread')
const messengerText = ref('Messenger')


</script>

<style scoped>
.user-viewport {
  height: 89.35vh;
}

.sidebar {
  padding: 1rem 0;
  width: 240px;
  background: linear-gradient(to bottom, #121212, 90%, #000000);
  flex-shrink: 0;
  border-top-right-radius: 30px;
  overflow: hidden;
  transition: .2s linear;
}

.sidebar.collapsed {
  width: 80px;
  transition: .2s linear;
}

main {
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  background-color: black;
}

.SDK {
  width: 100vw;
  height: 10.65vh;
  background-color: #121212;
}

.nav-item {
  height: 3rem;
}
.nav-link {
  height: 100%;
}

/* 기본 nav-link */
.nav-pills .nav-link {
  display: flex;
  color: #b3b3b3;
  /* 기본 텍스트 */
  background-color: #121212;
  /* 기본 배경 */
  border-radius: 0px;
  align-items: center;
  /* 세로가운데 */
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

header {
  height: 11.85vh;
  background-color: black;
}

.searchBox {
  margin-left: 2rem;
  background-color: #121212;
  width: 70%;
  height: 50%;
  border-radius: 3vh;
}

.searchBox>i {
  margin: 2rem;
  font-size: 3vh;
}

.profileBtn {
  width: 6vh;
  height: 6vh;
  background-color: #1ed760;
  border-radius: 100%;
  border: 1vh solid #121212;
  color: #121212;
  font-size: 2vh;
  font-weight: 700;
}

.profileBtn:hover {
  transform: scale(1.05);
  cursor: pointer;
  transition: .2s linear;
}

</style>
