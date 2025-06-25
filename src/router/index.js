import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import About from '../pages/About.vue'
import AthletesProfile from '../pages/AthletesProfile.vue'
import TrainingGoal from '../pages/TrainingGoal.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/athletsProfile', name: 'AthletsProfile', component: AthletesProfile  },
  { path: '/about', name: 'About', component: About },
  { path: '/TrainingGoal', name: 'TrainingGoal', component: TrainingGoal  } // Redirect all unmatched routes to Home
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router