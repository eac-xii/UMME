import HomeView from '@/views/HomeView.vue'
import MessengerView from '@/views/MessengerView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ThreadCreateView from '@/views/ThreadCreateView.vue'
import ThreadDetailView from '@/views/ThreadDetailView.vue'
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
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/threads/create',
      name: 'thread-create',
      component: ThreadCreateView
    },
    {
      path: '/threads/:id',
      name: 'thread-detail',
      component: ThreadDetailView
    },
    {
      path: '/messenger',
      name: 'messenger',
      component: MessengerView
    },
  ],
})

export default router
