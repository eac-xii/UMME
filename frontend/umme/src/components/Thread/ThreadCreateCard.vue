<template>
  <div class="createCard rounded-5 p-4">
    <div class="row">
      <div class="col-4 p-3">
        <img :src="props.track?.image">
      </div>
      <div class="col-8">
        <div class="d-flex justify-content-start align-items-center ms-auto text-decoration-none my-3">
          <div class="profileBtn d-flex justify-content-center align-items-center rounded-circle me-4">
            <span>{{ account.user?.last_name[0].toUpperCase() }}</span>
          </div>
          <span>{{ account.user?.last_name }} {{ account.user?.first_name }}</span>
        </div>
        <hr>
        <div class="py-4">
          <p>Title <span class="mx-2">|</span> {{ props.track?.name }}</p>
          <p>Artist <span class="mx-2">|</span> {{ props.track?.artists.map(artist => artist.name).join(', ') }}</p>
          <p></p>
        </div>
      </div>
    </div>
    <div class="row">
      <textarea class="col m-3 rounded-4 p-3" v-model="content">
      </textarea>
    </div>
    <div class="row">
      <div class="col">
        <button class="btn bgGreen" @click.prevent="uploadThread">Upload</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'
import { useThreadStore } from '@/stores/threads'

const account = useAccountStore()
const thread = useThreadStore()

const props = defineProps({
  track: Object,
})

const content = ref('')

const uploadThread = () => {
  if (props.track && content.value) {
    const payload = {
      content: content.value,
      track_id: props.track.spotify_id
    }
    thread.uploadThread(payload)
    content.value = ''
  }
}

</script>

<style scoped>
.createCard {
  background-color: #121212;
}

img {
  width: 100%;
  border-radius: 2vh;
}

.profileBtn {
  width: 3vh;
  height: 3vh;
  background-color: #1ed760;
  color: #121212;
  font-weight: 700;
}

textarea {
  height: 30vh;
  background-color: #333;
  border: none;
  color: #aaa;
  outline: none;
}
.bgGreen {
  background-color: #1ed760;
  width: 100%;
}
</style>