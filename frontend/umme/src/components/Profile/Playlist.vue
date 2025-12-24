<template>
  <div class="row px-4 wrapper">
    <div class="col">
      <div class="row sticky-top">
        <div class="col-1 align-center">
          <span>#</span>
        </div>
        <div class="col-9">
          <span>Title</span>
        </div>
        <div class="col-2 align-center">
          <i class="bi bi-clock"></i>
        </div>
        <hr>
      </div>
      <div class="row p-2 mb-1 item rounded-2" v-for="item, index in playlist">
        <div class="col-1 align-center">
          <span>{{ index + 1 }}</span>
        </div>
        <div class="col-9 d-flex align-items-center">
          <div
            class="album"
            :style="{'background-image': `url('${item.track?.image}')`}"
          >
          </div>
          <div class="d-flex flex-column ms-2">
            <span class="track">{{ item.track?.name }}</span>
            <span class="artist">{{ tool.formatArtists(item.track?.artists) }}</span>
          </div>
        </div>
        <div class="col-2 align-center">
          {{ tool.formatTime(item.track?.duration_ms / 1000)}}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useAccountStore } from '@/stores/accounts'
import { useToolStore } from '@/stores/tools'

const account = useAccountStore()
const tool = useToolStore()

const props = defineProps({
  userId: String
})

const playlist = ref(null)

const loading = ref(true)
const error = ref(false)
watch(
  () => props.userId,
  async id => {
    if (!id) return
    try {
      playlist.value = await account.getPlaylist(id)
    } catch {
      error.value = true
    } finally {
      loading.value = false
    }
  },
  { immediate: true }
)
</script>

<style scoped>
.wrapper {
  max-height: 55vh;
  overflow-y: auto;
}
.sticky-top {
  background-color: #000;
}
.album {
  width: 5vh;
  height: 5vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  border-radius: .5vh;
}
.track {
  color: #aaa;
}
.artist {
  color: #8c8c8c;
  font-size: 1.5vh;
}
.align-center {
  display: flex;
  align-items: center;
}
.item:hover {
  transition: .5s ease;
  background-color: #242424;
  cursor: pointer;
}
</style>