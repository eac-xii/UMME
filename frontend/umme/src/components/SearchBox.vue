<template>
  <div class="searchBox d-flex align-items-center">
    <i class="bi bi-search"></i>|
    <div class="dropdown searchDrop">
      <input id="searchInput" type="text" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"
        placeholder="What do you want to play?" autocomplete="off" @keyup="search" v-model.trim="query">
      <ul class="dropdown-menu w-75">
        <li v-for="item in dropdownItems" :key="item.data.id" class="my-1">
          <a href="#" class="dropdown-item">
            <div v-if="item.type === 'artist'" class="d-flex align-items-center">
              <img class="artistImg" :src="item.data.images[0]?.url">
              <div class="artistDetail mx-2 d-flex flex-column">
                <p class="itemName">{{ item.data.name }}</p>
                <p class="itemType">{{ item.type.toUpperCase() }}</p>
              </div>
              <button
                class="ms-auto btn btn-outline-secondary border-0 rounded-circle searchByArtistBtn d-flex justify-content-center align-items-center"
                @click.prevent="searchArtistTracks(item.data.id)">
                <span class="text-white-50">
                  >
                </span>
              </button>
            </div>
            <div v-if="item.type === 'track'" class="d-flex align-items-center">
              <img class="trackImg" :src="item.data.album.images[0]?.url">
              <div class="trackDetail mx-2 d-flex flex-column">
                <p class="itemName">{{ item.data.name }}</p>
                <p class="trackArtists"><span class="itemType">{{ item.type.toUpperCase() }} · </span>{{
                  item.data.artists.map(artist => artist.name).join(', ')}}</p>
              </div>
              <button
                class="ms-auto btn btn-outline-secondary border-0 rounded-circle addTrackToPlaylistBtn d-flex justify-content-center align-items-center"
                @click.prevent="addTrackToPlaylist(item.data)">+</button>
            </div>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useToolStore } from '@/stores/tools'
import { useAccountStore } from '@/stores/accounts'

const router = useRouter()
const tool = useToolStore()
const account = useAccountStore()

const query = ref('')
const dropdownItems = computed(() => tool.searchItems)

const search = async () => {
  const payload = {
    query: query.value
  }
  await tool.search(payload)
}

const searchArtistTracks = async (artistId) => {
  const payload = {
    artistId
  }
  await tool.searchArtistTracks(payload)
}

const addTrackToPlaylist = async (track) => {
  if (!account.user) {
    window.alert('Login first!')
    router.replace({ name: 'login' })
    return
  }
  const payload = {
    track
  }
  await tool.addTrackToPlaylist(payload)
  await tool.getPlaylistItems()
}
</script>

<style scoped>
.searchBox {
  margin-left: 2rem;
  background-color: #121212;
  width: 70%;
  height: 50%;
  border-radius: 3vh;
}

.searchDrop {
  flex-grow: 1;
}

.searchDrop>ul {
  background-color: #121212;
}

.searchDrop>ul>li>a:hover {
  background-color: #404040;
}

.searchDrop>ul>li>a {
  color: #bbb;
}

.searchBox>i {
  margin: 2rem;
  font-size: 2vh;
}

#searchInput {
  display: flex;
  background-color: #121212;
  border: none;
  width: 90%;
  margin: 0 2vw 0 2vw;
  outline: none;
  color: #bbb;
}

.searchDrop>.dropdown-menu {
  border-radius: 0 0 1vh 1vh;
  border-left: 3px solid rgba(128, 128, 128, 80%);
  height: 20vh;
  overflow-y: scroll;
}

.searchDrop>.dropdown-menu::-webkit-scrollbar {
  background-color: rgba(64, 64, 64, 80%);
  border-radius: 1vh;
}

.searchDrop>.dropdown-menu::-webkit-scrollbar-thumb {
  background-color: rgba(128, 128, 128, 80%);
  border-radius: 1vh;
  right: 20px;
}

.searchByArtistBtn,
.addTrackToPlaylistBtn {
  width: 2vh;
  height: 2vh;
}

.artistImg {
  width: 4vw;
  height: 4vw;
  border-radius: 100%;
}

.dropdown-item>div>div>p {
  margin: 0;
  padding: 0;
}

.trackImg {
  width: 4vw;
  height: 4vw;
  border-radius: 0.5vw;
}

.trackArtists {
  font-size: 1vw;
  overflow: hidden;
}

.itemName {
  font-size: 1.25vw;
}

.itemType {
  color: #8c8c8c;
  font-size: 1vw;
}
</style>