import { defineStore } from 'pinia'
import api from '@/api/axios'
import { ref } from 'vue'

export const useToolStore = defineStore('tool', () => {
  const searchItems = ref([])
  const playlist = ref([])

  const search = async (payload) => {
    const { query } = payload
    try {
      const response = await api.get('/musics/spotify/search/', {
        params: { query },
      })
      searchItems.value = response.data
    } catch (error) {
      console.error(error)
    }
  }

  const searchArtistTracks = async (payload) => {
    const { artistId } = payload
    try {
      const response = await api.get(
        '/musics/spotify/search_artist_tracks/',
        { params: { artistId } }
      )
      searchItems.value = response.data
    } catch (error) {
      console.error(error)
    }
  }

  const addTrackToPlaylist = async (payload) => {
    const { track } = payload
    try {
      await api.post('/musics/spotify/add_track_to_playlist/', { track })
    } catch (error) {
      console.error(error)
    }
  }

  const getPlaylistItems = async () => {
    try {
      const response = await api.get('/musics/get_playlist_items/')
      playlist.value = response.data
    } catch (error) {
      console.error(error)
    }
  }

  return {
    searchItems,
    playlist,

    search,
    searchArtistTracks,
    addTrackToPlaylist,
    getPlaylistItems,
  }
})
