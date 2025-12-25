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
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useThreadStore } from '@/stores/threads'

const threadStore = useThreadStore()
const route = useRoute()

const userId = route.params.id

const Acousticness = ref(0)
const Danceability = ref(0)
const Energy = ref(0)
const Sentiment = ref(0)


const FEATURES = {
  acousticness: 'Acousticness',
  danceability: 'Danceability',
  energy: 'Energy',
  valence: 'Sentiment'
}


const calculateAverages = featuresList => {
  const sums = {
    acousticness: 0,
    danceability: 0,
    energy: 0,
    valence: 0
  }

  let count = 0

  for (const features of featuresList) {
    if (!features) continue

    let valid = false

    for (const key in sums) {
      if (typeof features[key] === 'number') {
        sums[key] += features[key]
        valid = true
      }
    }

    if (valid) count++
  }

  if (count === 0) count = 1

  return Object.fromEntries(
    Object.entries(sums).map(([k, v]) => [k, Math.round((v / count) * 100)])
  )
}

onMounted(async () => {
  const threads = await threadStore.getUserThreads({ userId })

  const featureRequests = threads.map(t =>
    threadStore.getAudiofeatures({ track_id: t.track.id })
  )

  const featuresList = await Promise.all(featureRequests)

  const averages = calculateAverages(featuresList)

  Acousticness.value = averages.acousticness
  Danceability.value = averages.danceability
  Energy.value = averages.energy
  Sentiment.value = averages.valence
})

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
