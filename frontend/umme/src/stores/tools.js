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

  const formatTime = (sec) => {
    if (!sec && sec !== 0) return '0:00'
    const m = Math.floor(sec / 60)
    const s = String(Math.floor(Math.abs(sec) % 60)).padStart(2, '0')
    return `${m}:${s}`
  }

  const formatArtists = (artists) => {
    return artists?.map(artist => artist.name).join(' · ')
  }

  const getElapsedTime = (isoString) => {
  if (!isoString) return ''
  const diffMs = new Date() - new Date(isoString)
  const diffMin = Math.floor(diffMs / 60000)
  const diffHour = Math.floor(diffMin / 60)
  const diffDay = Math.floor(diffHour / 24)

  if (diffMin < 1) return 'now'
  if (diffMin < 60) return `${diffMin} minutes ago`
  if (diffHour < 24) return `${diffHour} hours ago`
  return `${diffDay} days ago`
}

  return {
    searchItems,
    playlist,

    search,
    searchArtistTracks,
    addTrackToPlaylist,
    getPlaylistItems,
    formatTime,
    formatArtists,
    getElapsedTime,
  }
})
