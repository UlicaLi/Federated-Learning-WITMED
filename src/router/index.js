import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import UserSignup from '../views/UserSignup.vue'
// import UserLogin from '../views/UserLogin.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/UserLogin.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: UserSignup
  },
  {
    // path: '/project/:name',
    path: '/project/:name',
    name: 'project',
    component: () => import('../views/ProjectView.vue')
  },
  {
    path: '/admin',
    name: 'admin',
    component: () => import('../views/AdminView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
