<template>
  <div class="row features-container ms-1 me-2">
    <div class="feature">
      <div class="title">Acousticness</div>
      <div class="progress-bar">
        <div class="progress Acousticness" :style="{ width: Acousticness + '%' }"></div>
      </div>
    </div>
    <div class="feature">
      <div class="title">Sentiment</div>
      <div class="progress-bar">
        <div class="progress Sentiment" :style="{ width: Sentiment + '%' }"></div>
      </div>
    </div>
    <div class="feature">
      <div class="title">Energy</div>
      <div class="progress-bar">
        <div class="progress Energy" :style="{ width: Energy + '%' }"></div>
      </div>
    </div>
    <div class="feature">
      <div class="title">Danceability</div>
      <div class="progress-bar">
        <div class="progress Danceability" :style="{ width: Danceability + '%' }"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const Acousticness = ref(70)
const Danceability = ref(20)
const Energy = ref(50)
const Sentiment = ref(15)
</script>

<style scoped>
.features-container {
  height: 100%;
  background: linear-gradient(to bottom, #121212, 50%, #000);
  border-top-left-radius: 3vh;
  border-top-right-radius: 3vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 1.4rem;
  padding: 2rem;
}

.feature {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.title {
  width: 6rem;
  text-align: center;
  font-size: 1rem;
  color: #aaa;
}

.progress-bar {
  flex-grow: 1;
  height: 1.2rem;
  background-color: #eee;
  border-radius: 0.5rem;
  overflow: hidden;
}

.progress {
  height: 100%;
  border-radius: 0.5rem 0 0 0.5rem;
}

.Acousticness {
  background-color: #8FD917;
}

.Danceability {
  background-color: #1799D9;
}

.Energy {
  background-color: #A217D9;
}

.Sentiment {
  background-color: #D91765;
}
</style>
