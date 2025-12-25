<template>
  <div class="container-fluid d-flex justify-content-center align-items-center">
    <form
      ref="formRef"
      class="w-50 needs-validation"
      novalidate
      @submit.prevent="logIn"
    >
      <h2>Log In</h2>
      <hr>

      <div class="mb-3">
        <label class="form-label">Email</label>
        <input
          type="email"
          class="form-control"
          v-model="email"
          :class="emailClass()"
          required
        >
        <div class="invalid-feedback">
          Please enter a valid email address.
        </div>
      </div>

      <div class="mb-3">
        <label class="form-label">Password</label>
        <input
          type="password"
          class="form-control"
          v-model="password"
          :class="passwordClass()"
          required
        >
        <div class="invalid-feedback">
          Password is required.
        </div>
      </div>

      <div v-if="serverError" class="text-danger small mb-3">
        {{ serverError }}
      </div>

      <div class="mb-3 d-flex justify-content-between">
        <button type="submit" class="btn btn-outline-light">
          Submit
        </button>

        <RouterLink :to="{ name: 'signup' }">
          <button type="button" class="btn btn-outline-secondary">
            Sign Up
          </button>
        </RouterLink>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

const account = useAccountStore()
const formRef = ref(null)

const email = ref('')
const password = ref('')
const submitted = ref(false)
const serverError = ref('')

const emailClass = () => {
  if (!submitted.value && !email.value) return ''
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)
    ? 'is-valid'
    : 'is-invalid'
}

const passwordClass = () => {
  if (!submitted.value && !password.value) return ''
  return password.value.trim()
    ? 'is-valid'
    : 'is-invalid'
}

const logIn = async () => {
  submitted.value = true
  serverError.value = ''

  const form = formRef.value

  if (!form.checkValidity()) {
    form.classList.add('was-validated')
    return
  }

  try {
    await account.logIn({
      email: email.value,
      password: password.value
    })
    window.location.href = '/'
  } catch (err) {
    serverError.value = 'Invalid email or password.'
  }
}
</script>


<style scoped></style>