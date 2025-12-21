<template>
  <div>
    절대 누르면 안될것 같은 <button @click.prevent="logOut">버튼</button>
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
</script>

<style scoped>

</style>