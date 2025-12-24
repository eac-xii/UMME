<template>
  <div class="card text-bg-dark">
    <img :src="thread.track?.image" class="card-img" alt="album cover">

    <div class="card-img-overlay overlay">
      <div class="track-title">
        <h5 class="card-title">
          {{ thread.track?.name }}
        </h5>
      </div>
    </div>
  </div>
</template>


<script setup>
const props = defineProps({
  thread: Object,
})
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
  transform: translateY(-4px) scale(1.02); 
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35);
}
</style>