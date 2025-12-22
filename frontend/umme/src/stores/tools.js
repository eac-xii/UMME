import { defineStore } from 'pinia'
import api from '@/api/axios'

export const useToolStore = defineStore('tool', {
  state: () => ({
    searchItems: [],
    playlist: []
  }),

  actions: {
    async search(payload) {
      const { query } = payload
      try {
        const response = await api.get('/musics/spotify/search/', {
          params: { query }
        })
        this.searchItems = response.data
      } catch (error) {}
    },
    async searchArtistTracks(payload) {
      const { artistId } = payload
      try {
        const response = await api.get('/musics/spotify/search_artist_tracks/', {
          params: { artistId }
        })
        this.searchItems = response.data
      } catch (error) {}
    },
    addTrackToPlaylist(payload) {
      const { track } = payload
      api.post('/musics/spotify/add_track_to_playlist/', { track })
    },
    async getPlaylistItems() {
      try {
        const response = await api.get('/musics/get_playlist_items/')
        this.playlist = response.data
        console.log(response.data)
      } catch (error) {}
    }
  }
})