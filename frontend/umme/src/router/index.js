import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ThreadCreateView from '@/views/ThreadCreateView.vue'
import ThreadDetailView from '@/views/ThreadDetailView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'
import { useToolStore } from '@/stores/tools'
import { useThreadStore } from '@/stores/threads'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView,
      meta: { requiresAuth: true }
    },
    {
      path: '/threads/create',
      name: 'thread-create',
      component: ThreadCreateView,
      meta: { requiresAuth: true }
    },
    {
      path: '/threads/:id',
      name: 'thread-detail',
      component: ThreadDetailView,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
  ],
})

router.beforeEach(async (to) => {
    const account = useAccountStore()
    const tool = useToolStore()
    const thread = useThreadStore()

    if (!account.checked || !account.user?.is_spotify) {
       await account.checkAuth()
    }
    
    if (account.isAuthenticated) {
      await tool.getPlaylistItems()
    }

    if ((to.name === 'login' || to.name === 'signup') && account.isAuthenticated) {
      window.alert('You\'ve already logged in!')
      return { name: 'home' }
    }

    if (to.meta.requiresAuth && !account.isAuthenticated) {
      return { name: 'login' }
    }
})

export default router
