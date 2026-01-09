<template>
  <v-main class="gradient-bg">
    <v-card class="rounded-0">
      <!-- Title with icons -->
      <span class="title-runplan text-h">
        <v-icon size="40">mdi-run</v-icon>
        <span>Run Plan Generator</span>
        <v-icon size="40">mdi-run-fast</v-icon>
      </span>
      <!-- Subtitle under the title -->
      <span class="title-runplan2">
        Create your personalized running plan in minutes!
      </span>
    </v-card>

    <v-container class="text-center">
      <v-row style="display: flex" justify="center">
        <v-card
          class="athlets-card"
          prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg"
          variant="elevated"
          elevation="7"
        >
          <!-- TITLE -->
          <template #title>
            <span> Training Goal </span>
          </template>

          <!-- SUBTITLE -->
          <template #subtitle>
            <span style="color: #001f3f">
              Set you goal race and training preferences
            </span>
          </template>
        </v-card>
      </v-row>

      <v-row class="choosing-fields">
        <v-col sm="4">
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
              goal.targetDate ? goal.targetDate.toISOString().slice(0, 10) : ''
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

          <div class="d-flex justify-space-between">
            <v-btn
              color="#001f3f"
              class="mt-5"
              rounded
              elevation="16"
              @click="$router.back()"
            >
              <v-icon size="20">mdi-arrow-left-box</v-icon>Back
            </v-btn>
            <v-btn
              color="#001f3f"
              class="mt-5"
              rounded
              elevation="16"
              @click="goNext()"
              >Review <v-icon size="20">mdi-arrow-right-box</v-icon></v-btn
            >
          </div>
        </v-col>
      </v-row>
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
