<template>
    <div class="container-fluid d-flex justify-content-center align-items-center">
        <form class="w-50" @submit.prevent="logIn">
            <h2>Log In</h2>
            <hr>
            <div class="mb-3">
                <label for="inputEmail" class="form-label">Email</label>
                <input type="text" id="inputEmail" class="form-control" v-model="email">
            </div>
            <div class="mb-3">
                <label for="inputPassword" class="form-label">Password</label>
                <input type="password" id="inputPassword" class="form-control" v-model="password">
            </div>
            <div class="mb-3 d-flex justify-content-between">
                <button type="submit" class="btn btn-outline-light">Submit</button>
                <RouterLink :to="{ name: 'signup' }">
                    <button class="btn btn-outline-secondary">
                        Sign Up
                    </button>
                </RouterLink>
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'
const account = useAccountStore()
const router = useRouter()

const email = ref('')
const password = ref('')

const logIn = async () => {
    const payload = {
        email: email.value,
        password: password.value
    }
    await account.logIn(payload)
    router.push({ name: 'home' })
}
</script>

<style scoped>

</style>