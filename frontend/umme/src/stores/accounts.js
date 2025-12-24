import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/api/axios'

export const useAccountStore = defineStore('account', () => {
    const user = ref(null)
    const isAuthenticated = ref(false)
    const checked = ref(false)

    const checkAuth = async () => {
        try {
            const res = await api.get('/accounts/user/')
            user.value = res.data
            isAuthenticated.value = true
        } catch {
            user.value = null
            isAuthenticated.value = false
        } finally {
            checked.value = true
        }
        return isAuthenticated.value
    }

    const logIn = async (payload) => {
        await api.post('/accounts/login/', payload)
        isAuthenticated.value = true
        checked.value = true
    }

    const signUp = async (payload) => {
        await api.post('/accounts/registration/', payload)
    }

    const logOut = async () => {
        await api.post('/accounts/logout/')
        user.value = null
        isAuthenticated.value = false
        checked.value = false
    }

    const initUserSetting = async () => {
        try {
            await api.post('/accounts_umme/init_user_settings/')
        } catch (error) {
            console.error(error)
        }
    }

    const updateProfile = async (payload) => {
        try {
            const response = await api.put('/accounts_umme/update_profile/', payload)   
            console.log(response.data)
        } catch (error) {
            console.error(error)
        }
    }

    const connectSpotify = () => {
        if (!user.value) return

        const clientId = import.meta.env.VITE_CLIENT_ID
        const redirectURI = import.meta.env.VITE_REDIRECT_URI
        const scope =
            'streaming user-read-email user-read-private user-modify-playback-state user-read-recently-played user-read-playback-state'

        const state = btoa(JSON.stringify({ user_id: user.value.pk }))

        const url =
            'https://accounts.spotify.com/authorize?' +
            new URLSearchParams({
                response_type: 'code',
                client_id: clientId,
                scope,
                redirect_uri: redirectURI,
                state,
            })

        window.location.href = url
    }

    const getProfile = async (userId) => {
        try {
            const response = await api.get(`/accounts_umme/get_profile/${userId}/`)
            return response.data
        } catch (error) {
            console.error(error)
        }
    }

    const getPlaylist = async (userId) => {
        try {
            const response = await api.get(`/accounts_umme/get_playlist/${userId}`)
            return response.data
        } catch (error) {
            console.error(error)
        }
    }

    return {
        user,
        isAuthenticated,
        checked,

        checkAuth,
        logIn,
        signUp,
        logOut,
        initUserSetting,
        updateProfile,

        connectSpotify,

        getProfile,
        getPlaylist,
    }
})
