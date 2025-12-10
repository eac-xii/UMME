import ChatView from '@/views/ChatView.vue'
import HomeView from '@/views/HomeView.vue'
import MessengerView from '@/views/MessengerView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ThreadView from '@/views/ThreadView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileView,
    },
    {
      path: '/thread',
      name: 'Thread',
      component: ThreadView
    },
    {
      path: '/messenger',
      name: 'Messenger',
      component: MessengerView
    },
    {
      path: '/chat/:userId',
      name: 'chatRoom',
      component: ChatView
    }
  ],
})

export default router
