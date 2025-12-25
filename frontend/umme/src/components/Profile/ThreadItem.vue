<template>
  <div class="thread-item">
    <div class="card text-bg-dark" @click="openModal">
      <img :src="thread.track?.image" class="card-img" alt="album cover">
  
      <div class="card-img-overlay overlay">
        <div class="track-title">
          <h5 class="card-title">
            {{ thread.track?.name }}
          </h5>
        </div>
      </div>
    </div>
    <Teleport to="body">
      <div v-if="open" class="sp-backdrop" @click="closeModal">
        <div class="sp-modal" @click.stop>
  
          <!-- HEADER -->
          <section
            class="sp-header"
            :style="{ backgroundImage: `url(${thread.track?.image})` }"
          >
            <div class="header-overlay">
              <img :src="thread.track?.image" class="cover" />
  
              <div class="header-info">
                <span class="type">THREAD</span>
                <h1>{{ thread.track?.name }}</h1>
  
                <div class="meta">
                  <span>{{ thread.user?.username }}</span>
                  <span>•</span>
                  <span>{{ formatDate(thread.created_at) }}</span>
                </div>
              </div>
            </div>
          </section>
  
          <!-- BODY -->
          <section class="sp-body">
            <p class="description">
              {{ thread.content }}
            </p>
  
            <!-- <button class="play-btn">▶ Play</button> -->
          </section>
  
        </div>
      </div>
    </Teleport>
  </div>
</template>


<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const props = defineProps({
  thread: Object,
})
const open = ref(false)
const openModal = () => (open.value = true)
const closeModal = () => (open.value = false)
// const router = useRouter()
// const threadDetail = () => {
//   router.push({
//     name: 'thread-detail',
//     params: { id: props.thread.id }
//   })
// }

const formatDate = (d) =>
  d ? new Date(d).toLocaleDateString() : ''
</script>

<style scoped>
.card {
  position: relative;
  overflow: hidden;
}

.card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* overlay 전체를 flex로 */
.overlay {
  display: flex;
  flex-direction: column;
  padding: 0;
}

.track-title {
  margin-top: auto;
  width: 100%;
  height: 40px;
  background-color: rgba(0, 0, 0, 0.5);
  padding: 0 0.6rem;

  display: flex;
  align-items: center;
}

.card-title {
  margin: 0;
  font-size: 1rem;
  font-weight: 300;
  color: white;

  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.card:hover .track-title {
  background-color: rgba(0, 0, 0, 0.9);
}
.card:hover {
  transform: scale(1.020); 
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35);
  transition: .2s ease-in;
}

/* MODAL */
.sp-modal {
  width: 900px;
  max-height: 85vh;
  background: #121212;
  border-radius: 10px;
  overflow: hidden;
  color: white;
}

/* HEADER */
.sp-header {
  height: 300px;
  background-size: cover;
  background-position: center;
}

.header-overlay {
  height: 100%;
  background: linear-gradient(
    rgba(0,0,0,0.2),
    rgba(18,18,18,1)
  );
  display: flex;
  align-items: flex-end;
  padding: 2rem;
  gap: 1.5rem;
}

.cover {
  width: 180px;
  height: 180px;
  object-fit: cover;
  box-shadow: 0 10px 30px rgba(0,0,0,0.7);
}

.header-info {
  display: flex;
  flex-direction: column;
}

.type {
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  color: #b3b3b3;
}

.header-info h1 {
  font-size: 2.8rem;
  font-weight: 800;
  margin: 0.3rem 0;
}

.meta {
  font-size: 0.9rem;
  color: #b3b3b3;
}

/* BODY */
.sp-body {
  padding: 2rem;
}

.description {
  font-size: 1rem;
  line-height: 1.7;
  color: #eaeaea;
  max-width: 80%;
}

.play-btn {
  margin-top: 2rem;
  background: #1db954;
  border: none;
  color: black;
  font-weight: 700;
  padding: 0.7rem 2.2rem;
  border-radius: 999px;
  font-size: 1rem;
  cursor: pointer;
}

.play-btn:hover {
  transform: scale(1.05);
}

.sp-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  z-index: 9999;

  display: flex;
  align-items: center;
  justify-content: center;
}
</style>