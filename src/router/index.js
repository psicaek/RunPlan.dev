import { createRouter, createWebHistory } from "vue-router";
import Home from "../pages/Home.vue";
import About from "../pages/About.vue";
import AthletesProfile from "../pages/AthletesProfile.vue";
import TrainingGoal from "../pages/TrainingGoal.vue";
import Review from "../pages/Review.vue";
import Info from "../pages/Info.vue";
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";

import Result from "../pages/Result.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  {
    path: "/athletsProfile",
    name: "AthletsProfile",
    component: AthletesProfile,
  },
  { path: "/about", name: "About", component: About },
  { path: "/TrainingGoal", name: "TrainingGoal", component: TrainingGoal },
  { path: "/review", name: "Review", component: Review },
  { path: "/Result", name: "Result", component: Result },
  { path: "/Info", name: "Info", component: Info },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const store = useRunnerProfileStore();

  if (to.name === "TrainingGoal") {
    if (!store.isProfileComplete()) {
      return next({ name: "AthletsProfile" }); // Αν δεν έχει συμπληρωθεί profile, γύρνα στο προφίλ
    }
  }
  if (to.name === "Review") {
    if (!store.isGoalComplete()) {
      return next({ name: "TrainingGoal" });
    }
  }

  next();
});

export default router;
