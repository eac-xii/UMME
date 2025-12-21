import { defineStore } from 'pinia'
import api from '@/api/axios'

export const useAccountStore = defineStore('account', {
    state: () => ({
        user: null,
        isAuthenticated: false,
        checked: false,
    }),

    actions: {
        async checkAuth() {
            try {
                const res = await api.get('/accounts/user/')
                this.user = res.data
                this.isAuthenticated = true
            } catch {
                this.user = null
                this.isAuthenticated = false
            } finally {
                this.checked = true
            }

            return this.isAuthenticated
        },
        async logIn(payload) {
            await api.post(
                '/accounts/login/',
                payload
            ).then(() => {
                this.isAuthenticated = true
                this.checked = true
            })
        },
        async signUp(payload) {
            await api.post(
                '/accounts/registration/',
                payload
            )
        },
        async logOut() {
            await api.post(
                '/accounts/logout/'
            ).then(() => {
                this.isAuthenticated = false
            })
        }
    }
})