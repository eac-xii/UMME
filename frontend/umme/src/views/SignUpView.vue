<template>
    <div class="container-fluid d-flex justify-content-center align-items-center">
        <form class="w-50" @submit.prevent="signUp">
            <div class="mb-3">
                <label for="inputEmail" class="form-label">Email</label>
                <input type="email" id="inputEmail" class="form-control" v-model="email">
            </div>
            <div class="mb-3">
                <label for="inputUsername" class="form-label">ID</label>
                <input type="text" id="inputUsername" class="form-control" v-model="username">
            </div>
            <div class="mb-3 row">
                <div class="col">
                    <label for="inputLastName" class="form-label">Last Name</label>
                    <input type="text" id="inputLastName" class="form-control" v-model="last_name">
                </div>
                <div class="col">
                    <label for="inputFirstName" class="form-label">First Name</label>
                    <input type="text" id="inputFirstName" class="form-control" v-model="first_name">
                </div>
            </div>
            <div class="mb-3">
                <label for="inputPassword1" class="form-label">Password</label>
                <input type="password" id="inputPassword1" class="form-control" v-model="password1">
            </div>
            <div class="mb-3">
                <label for="inputPassword2" class="form-label">Password Confirmation</label>
                <input type="password" id="inputPassword2" class="form-control" v-model="password2">
            </div>
            <button type="submit" class="btn btn-dark">Submit</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'
import { useRouter } from 'vue-router'
const account = useAccountStore()
const router = useRouter()

const email = ref('')
const username = ref('')
const last_name = ref('')
const first_name = ref('')
const password1 = ref('')
const password2 = ref('')

const signUp = async () => {
    const payload = {
        email: email.value,
        username: username.value,
        last_name: last_name.value,
        first_name: first_name.value,
        password1: password1.value,
        password2: password2.value
    }
    await account.signUp(payload)   
    router.push({ name: 'home' }) 
}

</script>

<style scoped>

</style>