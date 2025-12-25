<template>
    <div
        class="image"
        :style="{backgroundImage: `url('${props.imageUrl ? base_url + props.imageUrl : defaultUser}')`}"
    >
    </div>
</template>

<script setup>
import defaultUser from '@/assets/default-user.png'
const base_url = import.meta.env.VITE_API_BASE_URL
const props = defineProps({
    imageUrl: String
})

</script>

<style scoped>
.image {
    width: 100%;
    height: 100%;
    border-radius: 100%;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
</style>