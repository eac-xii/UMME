import ChatView from '@/views/ChatView.vue'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import MessengerView from '@/views/MessengerView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ThreadView from '@/views/ThreadView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { requiresAuth: true }
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: { requiresAuth: true }
    },
    {
      path: '/thread',
      name: 'thread',
      component: ThreadView,
      meta: { requiresAuth: true }
    },
    {
      path: '/messenger',
      name: 'messenger',
      component: MessengerView,
      meta: { requiresAuth: true }
    },
    {
      path: '/chat/:userId',
      name: 'chatRoom',
      component: ChatView,
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
    }
  ],
})

router.beforeEach(async (to) => {
    const account = useAccountStore()

    if (!account.checked) {
       await account.checkAuth()
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
