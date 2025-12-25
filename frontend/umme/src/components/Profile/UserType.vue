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
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useThreadStore } from '@/stores/threads';
import { useToolStore } from '@/stores/tools';

const thread = useThreadStore()
const userthreads = ref([])
const route = useRoute()

const userId = route.params.id
const Acousticness = ref(0)
const Danceability = ref(0)
const Energy = ref(0)
const Sentiment = ref(0)

onMounted(async () => {
  const payload = { userId }
  const data = await thread.getUserThreads(payload)

  let totalAcousticness = 0
  let totalDanceability = 0
  let totalEnergy = 0
  let totalValence = 0
  let validCount = 0

  userthreads.value = data
  for (const threadItem of userthreads.value) {
    const trackId = threadItem.track.id
    const features = await thread.getAudiofeatures({ track_id: trackId })

    if (features) { // 오디오 피처스가 존재할 때만 계산
        totalAcousticness += features.acousticness
        totalDanceability += features.danceability
        totalEnergy += features.energy
        totalValence += features.valence
        validCount++
      }
    console.log()
    const count = validCount || 1
    Acousticness.value = Math.round((totalAcousticness / count) * 100)
    Danceability.value = Math.round((totalDanceability / count) * 100)
    Energy.value = Math.round((totalEnergy / count) * 100)
    Sentiment.value = Math.round((totalValence / count) * 100)
  }
});
</script>

<style scoped>
  .aa {
    color: #eee;
  }
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
