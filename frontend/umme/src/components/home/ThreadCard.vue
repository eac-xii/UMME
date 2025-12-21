<template>
  <div class="thread-card d-flex p-4">
    <div class="songInfo mx-3">
      <div id="albumcover">Image</div>
      <div class="track-meta px-2">
        <p id="title">I Fall In Love Too Easily</p>
        <p id="artist">Chet Baker</p>
      </div>
    </div>
    <div class="thread-body px-3">
      <h5>{{ thread.title }}</h5>
      <p>{{ thread.content }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  'thread' : Object,
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