<template>
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
          <!-- Title & Subtitle -->
          <h1 class="text-h5 font-weight-bold mb-0">Run Plan Generator</h1>

          <p class="text-subtitle-2">
            Create your personalized running plan in minutes!
          </p>
        </v-col>
      </v-row>
    </v-container>
    <v-container class="title-text text-center white--text">
      <v-row>
        <v-col cols="12" sm="6" offset-sm="3">
          <p class="page-title-text">Training Goal</p>
          <p class="page-second-text">
            Set you goal race and training preferences.
          </p>
        </v-col>
      </v-row>
    </v-container>
    <v-container class="text-center">
      <v-card-text>
        <v-row justify="center">
          <v-col cols="12" sm="6">
            <div style="text-align: left; margin-bottom: 4px; font-weight: 500">
              Goal Race Distance
            </div>
            <v-select
              ref="Goal Race Distance"
              v-model="goal.raceDistance"
              :items="raceDistanceOptions"
              :rules="[() => !!raceDistanceOptions || 'This field is required']"
              class="mb-4"
              label="Goal Race Distance"
              variant="outlined"
              placeholder="e.g., 5K, 10K, Half Marathon, Marathon"
              color="blue"
            ></v-select>
            <div style="text-align: left; margin-bottom: 4px; font-weight: 500">
              Goal Time
            </div>
            <v-text-field
              v-model="goal.goalTime"
              label="Goal Time"
              variant="outlined"
              class="mb-4"
              placeholder="Enter time in minutes (20-300)"
              color="blue"
              type="text"
              min="14"
              max="300"
              :rules="[
                (v) => !!v || 'This field is required',
                (v) => /^[0-9]+$/.test(v) || 'Only numbers are allowed',
                (v) =>
                  (parseInt(v) >= 14 && parseInt(v) <= 300) ||
                  'Goal Time must be between 20 and 200 minutes',
              ]"
              clearable
            ></v-text-field>

            <div style="text-align: left; margin-bottom: 4px; font-weight: 500">
              Target Race Date
            </div>
            <v-text-field
              :model-value="
                goal.targetDate
                  ? goal.targetDate.toISOString().slice(0, 10)
                  : ''
              "
              @update:model-value="
                (val) => {
                  if (val) goal.targetDate = new Date(val);
                  else goal.targetDate = null;
                }
              "
              variant="outlined"
              class="mb-4"
              label="Select Target Date (YYYY-MM-DD)"
              color="blue"
              :rules="[
                (v) => (v && v.length > 0) || 'This field is required',
                (v) => {
                  if (!v) return true; // αν δεν έχει τιμή, το χειρίζεται ο πρώτος κανόνας
                  const selectedDate = new Date(v);
                  const today = new Date();
                  // μηδενίζουμε ώρες-λεπτά-δευτερόλεπτα για ακριβή σύγκριση ημερομηνιών μόνο
                  today.setHours(0, 0, 0, 0);
                  return selectedDate >= today || 'Date cannot be in the past';
                },
              ]"
              type="date"
            ></v-text-field>

            <div style="text-align: left; margin-bottom: 4px; font-weight: 500">
              Training Days Per Week
            </div>
            <v-select
              label="Training Days Per Week "
              v-model="goal.trainingDays"
              :items="allowedTrainingDays"
              :rules="[(v) => !!v || 'This field is required']"
              variant="outlined"
              class="mb-4"
              placeholder="e.g., 3 days"
              color="blue"
            ></v-select>

            <v-btn color="primary" class="mt-5" @click="$router.back()"
              >Back
            </v-btn>

            <v-btn color="success" class="mt-5" @click="goNext()">
              Review Inputs
            </v-btn>
          </v-col>
        </v-row>
      </v-card-text>
    </v-container>
  </v-main>
</template>
<script setup lang="ts">
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { computed } from "vue";
import "../assets/global.css";

const store = useRunnerProfileStore();
const { goal } = storeToRefs(store);
const { profile } = storeToRefs(store);
const router = useRouter();

const maxTrainingDaysPerLevel: Record<string, [number, number]> = {
  Beginner: [2, 3],
  Intermediate: [2, 5],
  Advanced: [4, 6],
  Expert: [4, 7],
  Elite: [5, 7],
};

const trainingDaysOptions = [
  "2 days",
  "3 days",
  "4 days",
  "5 days",
  "6 days",
  "7 days",
];

const allowedTrainingDays = computed(() => {
  const level = profile.value.experienceLevel;
  if (!level) return trainingDaysOptions; // no level selected yet

  const [minDays, maxDays] = maxTrainingDaysPerLevel[level];

  return trainingDaysOptions.filter((day) => {
    const numberOfDays = parseInt(day); // "3 days" -> 3
    return numberOfDays >= minDays && numberOfDays <= maxDays;
  });
});

const raceDistanceOptions = ["5K", "10K", "Half Marathon", "Marathon"];

function goNext() {
  if (store.isGoalComplete()) {
    router.push({ name: "Review" });
    console.log("next page ");
  } else {
    alert("Please complete all fields.");
    console.log("something is wrong");
  }
}
</script>
