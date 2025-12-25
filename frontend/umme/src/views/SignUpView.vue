<template>
    <div class="container-fluid d-flex justify-content-center align-items-center">
        <div v-if="loading" class="spinner-overlay d-flex flex-column justify-content-center align-items-center">
            <div class="spinner-border text-light mb-3" role="status"></div>
            <div class="text-light small">Setting up your account...</div>
        </div>
        <form ref="formRef" class="w-50 needs-validation" novalidate @submit.prevent="signUp">
            <h2>Sign Up</h2>
            <hr>
            <div class="mb-3">
                <label class="form-label">Email</label>
                <input type="email" class="form-control" v-model="email" :class="emailClass()" required>
                <div class="invalid-feedback">
                    Please enter a valid email address.
                </div>
            </div>
            <div class="mb-3">
                <label class="form-label">ID</label>
                <input type="text" class="form-control" v-model="username" :class="usernameClass()" required>
                <div class="invalid-feedback">
                    ID is required.
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col">
                    <label class="form-label">Last Name</label>
                    <input type="text" class="form-control" v-model="last_name" :class="nameClass(last_name)" required>
                    <div class="invalid-feedback">
                        Last name is required.
                    </div>
                </div>
                <div class="col">
                    <label class="form-label">First Name</label>
                    <input type="text" class="form-control" v-model="first_name" :class="nameClass(first_name)"
                        required>
                    <div class="invalid-feedback">
                        First name is required.
                    </div>
                </div>
            </div>
            <div class="mb-3">
                <label class="form-label">Password</label>
                <input type="password" class="form-control" v-model="password1" :class="passwordClass()" required>
                <div class="invalid-feedback">
                    Password must be at least 8 characters long.
                </div>
            </div>
            <div class="mb-3">
                <label class="form-label">Password Confirmation</label>
                <input type="password" class="form-control" v-model="password2" :class="passwordConfirmClass()"
                    required>
                <div class="invalid-feedback">
                    Passwords do not match.
                </div>
            </div>
            <button type="submit" class="btn btn-outline-light" :disabled="loading">
                Submit
            </button>
        </form>
    </div>
</template>


<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'

const account = useAccountStore()
const formRef = ref(null)

const email = ref('')
const username = ref('')
const last_name = ref('')
const first_name = ref('')
const password1 = ref('')
const password2 = ref('')
const submitted = ref(false)
const loading = ref(false)

const emailClass = () => {
    if (!submitted.value && !email.value) return ''
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)
        ? 'is-valid'
        : 'is-invalid'
}

const usernameClass = () => {
    if (!submitted.value && !username.value) return ''
    return username.value.trim()
        ? 'is-valid'
        : 'is-invalid'
}

const nameClass = value => {
    if (!submitted.value && !value) return ''
    return value.trim()
        ? 'is-valid'
        : 'is-invalid'
}

const passwordClass = () => {
    if (!submitted.value && !password1.value) return ''
    return password1.value.length >= 8
        ? 'is-valid'
        : 'is-invalid'
}

const passwordConfirmClass = () => {
    if (!submitted.value && !password2.value) return ''
    return password1.value === password2.value
        ? 'is-valid'
        : 'is-invalid'
}

const signUp = async () => {
    submitted.value = true
    const form = formRef.value

    if (!form.checkValidity() || password1.value !== password2.value) {
        form.classList.add('was-validated')
        return
    }

    loading.value = true
    try {
        const payload = {
            email: email.value,
            username: username.value,
            last_name: last_name.value,
            first_name: first_name.value,
            password1: password1.value,
            password2: password2.value
        }


        await account.signUp(payload)
        await account.logIn({ email: payload.email, password: payload.password1 })
        await account.initUserSetting()

        window.location.href = '/'
    } catch (err) {
        console.error(err)
        loading.value = false
    }
}
</script>

<style scoped>
.spinner-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 10;
}
</style>
