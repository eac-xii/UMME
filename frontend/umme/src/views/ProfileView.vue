<template>
  <div class="container-fluid d-flex justify-content-center align-items-center">
    <button class="btn btn-danger" @click.prevent="logOut">로그아웃</button>
    <button v-if="!account.user?.is_spotify" class="btn btn-success" @click.prevent="connectSpotify">스포티파이 연동하기</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'
const account = useAccountStore()
const router = useRouter()

const logOut = async () => {
  await account.logOut()
  router.push({ name: 'login' })
}

const connectSpotify = () => {
  account.connectSpotify()
}
</script>

<style scoped>

</style>