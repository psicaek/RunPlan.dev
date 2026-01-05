<template>
  <v-app>
    <v-main class="gradient-bg">
      <v-container style="max-width: 1900px">
        <v-row align="center" justify="center" class="mb-4">
          <!-- Logo -->
          <v-col cols="auto">
            <v-img
              src="src/assets/mainLogo.svg"
              alt="Run Plan Logo"
              width="60"
              class="mb-1"
            ></v-img>
          </v-col>
          <v-col>
            <h1 class="text-h5 font-weight-bold mb-0">Run Plan Generator</h1>
            <p class="text-subtitle-2">
              Review your inputs before generating your plan.
            </p>
          </v-col>
        </v-row>
      </v-container>

      <v-container class="page-second-text">
        <v-row>
          <v-col cols="12" sm="8" offset-sm="2" align="center">
            <h2>Athlete Profile</h2>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Experience Level:</v-list-item-title>
                <v-list-item-subtitle>{{
                  profile.experienceLevel || "-"
                }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>
                  Max Weekly Distance now :</v-list-item-title
                >
                <v-list-item-subtitle
                  >{{ profile.weeklyDistance }} km</v-list-item-subtitle
                >
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Longest Run ever :</v-list-item-title>
                <v-list-item-subtitle
                  >{{ profile.longestRun }} km</v-list-item-subtitle
                >
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Age:</v-list-item-title>
                <v-list-item-subtitle>{{ profile.age }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Gender:</v-list-item-title>
                <v-list-item-subtitle>{{
                  profile.gender
                }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
        </v-row>

        <v-row class="page-second-text">
          <v-col cols="12" sm="8" offset-sm="2" align="center">
            <h2>Training Goal</h2>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Race Distance:</v-list-item-title>
                <v-list-item-subtitle>{{
                  goal.raceDistance || "-"
                }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Goal Time:</v-list-item-title>
                <v-list-item-subtitle
                  >{{ goal.goalTime }} minutes</v-list-item-subtitle
                >
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Target Date:</v-list-item-title>
                <v-list-item-subtitle>{{
                  formattedTargetDate
                }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Training Days Per Week:</v-list-item-title>
                <v-list-item-subtitle>{{
                  goal.trainingDays || "-"
                }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
        </v-row>

        <v-row justify="center" class="mt-10">
          <v-col cols="auto">
            <v-btn color="primary" @click="goBack">Back</v-btn>
          </v-col>
          <v-col cols="auto">
            <v-btn color="success" @click="generatePlan()">Generate Plan</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { computed } from "vue";

const store = useRunnerProfileStore();
const router = useRouter();
const { profile, goal } = storeToRefs(store);

const formattedTargetDate = computed(() => {
  if (!goal.value.targetDate) return "-";
  const d =
    goal.value.targetDate instanceof Date
      ? goal.value.targetDate
      : new Date(goal.value.targetDate);
  return d.toLocaleDateString();
});

function goBack() {
  router.back();
}

function generatePlan() {
  // εδώ μπορείς να καλέσεις κάποιο action για δημιουργία προγράμματος
  // παράδειγμα πλοήγησης
  store.generateTrainingPlan();
  //router.push("/result");
}
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(to bottom, #00b4db, #001f3f);
  min-height: 100vh;
}
.page-title-text {
  font-size: 42px;
  font-family: Helvetica-Neue;
  color: #000000;
}
.page-second-text {
  font-size: 20px;
  font-family: Helvetica-Neue;
  color: #000000;
}
.white--text {
  color: white !important;
}
</style>
