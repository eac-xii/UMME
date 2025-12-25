<template>
  <div class="searchBox d-flex align-items-center">
    <i class="bi bi-search"></i>
    |
    <div class="dropdown searchDrop">
      <input
        id="searchInput"
        ref="searchInput"
        v-model.trim="query"
        type="text"
        class="dropdown-toggle"
        data-bs-toggle="dropdown"
        data-bs-auto-close="outside"
        :placeholder="account.isAuthenticated ? 'What do you want to play?' : 'Login required to use this search engine.'"
        autocomplete="off"
        @keyup="search"
        @focus="showDropdown"
        :disabled="!account.isAuthenticated"
      />

      <ul 
        ref="dropdownMenu"
        class="dropdown-menu w-75"
        v-show="query.length > 0 && dropdownItems.length > 0"
      >
        <li
          v-for="item in dropdownItems"
          :key="item.data.id"
          class="my-1"
        >
          <a href="#" class="dropdown-item">
            <div v-if="item.type === 'artist'" class="d-flex align-items-center">
              <img class="artistImg" :src="item.data.images[0]?.url" />
              <div class="artistDetail mx-2 d-flex flex-column">
                <p class="itemName">{{ item.data.name }}</p>
                <p class="itemType">{{ item.type.toUpperCase() }}</p>
              </div>
              <button
                class="ms-auto btn btn-outline-secondary border-0 rounded-circle searchByArtistBtn d-flex justify-content-center align-items-center"
                @click.prevent="searchArtistTracks(item.data.id)"
              >
                <span class="text-white-50">&gt;</span>
              </button>
            </div>

            <div v-if="item.type === 'track'" class="d-flex align-items-center">
              <img class="trackImg" :src="item.data.album.images[0]?.url" />
              <div class="trackDetail mx-2 d-flex flex-column">
                <p class="itemName">{{ item.data.name }}</p>
                <p class="trackArtists">
                  <span class="itemType">{{ item.type.toUpperCase() }} · </span>
                  {{ item.data.artists.map(a => a.name).join(', ') }}
                </p>
              </div>
              <button
                class="ms-auto btn btn-outline-secondary border-0 rounded-circle addTrackToPlaylistBtn d-flex justify-content-center align-items-center"
                @click.prevent.stop="addTrackToPlaylist(item.data)"
              >
                +
              </button>
            </div>
          </a>
        </li>
      </ul>
    </div>

    <button class="btn btn-outline-light border-0 rounded-pill AIbtn" @click="runAIMode">
      AI Search
    </button>
  </div>
</template>

<script setup>
import { ref, computed, watch, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import * as bootstrap from 'bootstrap'
import { useToolStore } from '@/stores/tools'
import { useAccountStore } from '@/stores/accounts'
import { useThreadStore } from '@/stores/threads'

const router = useRouter()
const tool = useToolStore()
const account = useAccountStore()
const thread = useThreadStore()

const query = ref('')
const searchInput = ref(null)
const dropdownMenu = ref(null)

const isAIMode = computed(() => thread.isAIMode)
const dropdownItems = computed(() => tool.searchItems)

watch(dropdownItems, async () => {
  await nextTick()
  if (dropdownMenu.value) {
    dropdownMenu.value.scrollTop = 0
  }
})

const search = async () => {
  if (!query.value?.trim()) {
    tool.searchItems = []
    return
  }
  await tool.search({ query: query.value })
}

const showDropdown = () => {
  if (query.value?.trim() && dropdownItems.value.length > 0) {
    if (searchInput.value) {
      const dropdownInstance = bootstrap.Dropdown.getOrCreateInstance(searchInput.value)
      dropdownInstance.show()
    }
  }
}

const searchArtistTracks = async (artistId) => {
  await tool.searchArtistTracks({ artistId })
}

const addTrackToPlaylist = async (track) => {
  if (!account.user) {
    window.alert('Login first!')
    router.replace({ name: 'login' })
    return
  }

  await tool.addTrackToPlaylist({ track })
  await tool.getPlaylistItems()

  if (searchInput.value) {
    const dropdownInstance = bootstrap.Dropdown.getOrCreateInstance(searchInput.value)
    dropdownInstance.hide()
  }
}

const runAIMode = async () => {
  if (!query.value) return
  await thread.runRag({ query: query.value })
}
</script>

<style scoped>
/* 기존 스타일 유지 */
.searchBox {
  margin-left: 2rem;
  background-color: #121212;
  width: 70%;
  height: 50%;
  border-radius: 3vh;
}
.searchDrop {
  position: relative;
  flex-grow: 1;
}
.searchDrop > ul {
  background-color: #121212;
}
.searchDrop > ul > li > a {
  color: #bbb;
}
.searchDrop > ul > li > a:hover {
  background-color: #404040;
}
.searchBox > i {
  margin: 2rem;
  font-size: 2vh;
}
#searchInput {
  display: flex;
  width: 90%;
  margin: 0 2vw;
  background-color: #121212;
  border: none;
  outline: none;
  color: #bbb;
}
.searchDrop > .dropdown-menu {
  left: 0 !important;
  transform: none !important;
  top: 100% !important;
  margin-top: 20px;
  max-height: 40vh;
  height: auto;
  overflow-y: auto;
  border-radius: 0 0 1vh 1vh;
  border-left: 3px solid rgba(128, 128, 128, 0.8);
}
.searchDrop > .dropdown-menu::-webkit-scrollbar {
  background-color: rgba(64, 64, 64, 0.8);
  border-radius: 1vh;
}
.searchDrop > .dropdown-menu::-webkit-scrollbar-thumb {
  background-color: rgba(128, 128, 128, 0.8);
  border-radius: 1vh;
}
.searchByArtistBtn,
.addTrackToPlaylistBtn {
  width: 2vh;
  height: 2vh;
}
.artistImg {
  width: 4vw;
  height: 4vw;
  border-radius: 50%;
}
.trackImg {
  width: 4vw;
  height: 4vw;
  border-radius: 0.5vw;
}
.dropdown-item p {
  margin: 0;
  padding: 0;
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
.AIbtn {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 8em;
  height: 2em;
  font-size: 0.8em;
  margin-right: 2rem;
}
</style>