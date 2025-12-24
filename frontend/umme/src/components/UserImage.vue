<template>
    <div
        class="image"
        :style="{backgroundImage: `url('${props.user?.image ? base_url + props.user?.image : defaultUser}')`}"
    >
    </div>
</template>

<script setup>
import defaultUser from '@/assets/default-user.png'
const base_url = import.meta.env.VITE_API_BASE_URL
const props = defineProps({
    user: Object
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