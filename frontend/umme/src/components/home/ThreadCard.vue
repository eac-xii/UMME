<template>
  <div class="thread-card d-flex p-4">
    <div class="songInfo mx-3">
      <img :src="thread.track?.image" id="albumcover">
      <div class="track-meta px-2">
        <p id="title">{{ thread.track?.name }}</p>
        <p id="artist">{{thread.track?.artists.map(artist => artist.name).join(', ')}}</p>
      </div>
    </div>
    <div class="thread-body px-3">
      <div class="userinfo d-flex flex-row">
        <div class="profileBtn d-flex justify-content-center align-items-center rounded-circle me-4">
          <span>{{ thread.user?.last_name[0].toUpperCase() }}</span>
        </div>
        <div class="d-flex flex-column">
          <p>{{ thread.user?.last_name }} {{ thread.user?.first_name }}</p>
          <p>{{ thread.updated_at }}</p>
        </div>
      </div>
      <hr>
      <p>{{ thread.content }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  'thread': Object,
})
</script>

<style scoped>
p {
  padding: 0;
  margin: 0;
}

.thread-card {
  height: 18rem;
  border-radius: 1rem;
  background-color: #121212;
  overflow: hidden;
}

.thread-body {
  flex-grow: 1;
  flex-direction: column;
}

.songInfo {
  width: 12rem;
  flex: 0 0 auto;
  align-items: center;
  justify-content: center;
  text-align: start;
  border-radius: 1rem;
  overflow: hidden;
}

.profileBtn {
  background-color: #1ed760;
  width: 3vh;
  height: 3vh;
  border-radius: 3vh;
  color: black;
  font-weight: 700;

}

#albumcover {
  text-align: center;
  width: 100%;
  aspect-ratio: 1;
  background-color: aquamarine;
  border-radius: 1rem;
  margin-bottom: 0.5rem;
}

#title {
  font-size: 0.7em;
  color: #eee;
}

#artist {
  font-size: 0.5em;
}
</style>