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
                this.checked = false
            })
        },
        connectSpotify() {
            const clientId = import.meta.env.VITE_CLIENT_ID
            const redirectURI = import.meta.env.VITE_REDIRECT_URI
            const scope = 'web-playback streaming user-read-email user-read-private user-modify-playback-state user-read-playback-state'

            const userId = this.user.pk
            const state = btoa(JSON.stringify({ user_id: userId }))

            const url = 
                'https://accounts.spotify.com/authorize?' +
                new URLSearchParams({
                    response_type: 'code',
                    client_id: clientId,
                    scope: scope,
                    redirect_uri: redirectURI,
                    state
                })
            window.location.href = url
        }
    }
})