<template>
  <div class="user-viewport d-flex">
    <aside class="sidebar">
      <div class="nav-brand" @click="collapsed = !collapsed">
        <PhCow :size="32" class="mx-2" />
        <span class="mx-2">UMME</span>
      </div>

      <ul class="nav nav-pills flex-column">
        <li class="nav-item">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'home' }">
            <PhHouse size="20" weight="regular" class="mx-3" />
            <span>Home</span>
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'thread-create' }">
            <PhNotePencil size="20" weight="regular" class="mx-3" />
            <span>Thread</span>
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" active-class="active" :to="{ name: 'messenger' }">
            <PhMessengerLogo size="20" weight="regular" class="mx-3" />
            Messenger
          </RouterLink>
        </li>
      </ul>
      <hr class="m-4">
      <Playlist @evoke-track="playTrack" />
    </aside>
    <main class="flex-grow-1">
      <header class="top d-flex align-items-center px-3">
        <SearchBox />
        <button v-if="account.isAuthenticated" class="btn btn-outline border-0" @click.prevent="logOut">
          로그아웃
        </button>
        <button v-if="!account.user?.is_spotify && account.isAuthenticated" class="btn btn-outline" @click.prevent="connectSpotify">
          스포티파이 연동하기
        </button>
        <RouterLink v-if="!account.isAuthenticated" :to="{ name: 'login'}">
          <button class="btn btn-light rounded-pill px-4 py-2 ms-4">
            로그인하기
          </button>
        </RouterLink>
        <RouterLink v-if="account.isAuthenticated" :to="{ name: 'profile' }"
          class="profileBtn d-flex justify-content-center align-items-center ms-auto text-decoration-none">
          <span>{{ account.user?.last_name[0].toUpperCase() }}</span>
        </RouterLink>
      </header>
      <RouterView />
    </main>
  </div>

  <div class="SDK position-fixed bottom-0 start-0 d-flex justify-content-center align-items-center">
    <SDKPlayer v-if="account.user?.is_spotify && account.isAuthenticated" />
    <div v-if="!account.user?.is_spotify || !account.isAuthenticated">
      Spotify Premium 사용자만 플레이어를 이용하실 수 있습니다.
    </div>
  </div>

</template>

<script setup>
import SDKPlayer from '@/components/SDKPlayer.vue'
import SearchBox from './components/SearchBox.vue'
import Playlist from './components/Playlist.vue'
import { useAccountStore } from '@/stores/accounts'
import { useControlStore } from './stores/controls'
import { useToolStore } from '@/stores/tools'
import { RouterLink, RouterView } from 'vue-router'
import { PhHouse, PhNotePencil, PhMessengerLogo, PhCow } from '@phosphor-icons/vue'
import { onMounted } from 'vue'

const account = useAccountStore()
const control = useControlStore()
const tool = useToolStore()

onMounted(() => {
  window.onSpotifyWebPlaybackSDKReady = () => {
  control.sdkReady = true
  }
})

const logOut = async () => {
  await account.logOut()
  tool.playlist = ''
  router.push({ name: 'login' })
}

const connectSpotify = () => {
  account.connectSpotify()
}

const playTrack = async (track) => {
  const payload = {
    spotify_id: track.spotify_id
  }
  await control.playTrack(payload)
}

</script>

<style scoped>
.user-viewport {
  height: 89.35vh;
}

.sidebar {
  padding: 1rem 0;
  width: 20vh;
  background-color: #121212;
  flex-shrink: 0;
  border-top-right-radius: 30px;
  overflow: hidden;
}

main {
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  background: black;
}

.SDK {
  width: 100vw;
  height: 10.65vh;
  background-color: black;
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

.profileBtn {
  width: 6vh;
  height: 6vh;
  background-color: #1ed760;
  border-radius: 100%;
  border: 1vh solid #121212;
  color: #121212;
  font-size: 1.5vh;
  font-weight: 700;
}

.profileBtn:hover {
  transform: scale(1.05);
  cursor: pointer;
  transition: .2s linear;
}
</style>
