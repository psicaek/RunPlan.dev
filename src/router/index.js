import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Generator from '../pages/Generator.vue'
import About from '../pages/About.vue'
import { fromJSON } from 'postcss'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/generate', name: 'Generate', component: Generator },
  { path: '/about', name: 'About', component: About },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router