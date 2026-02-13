<template>
  <BaseCard></BaseCard>>

  <v-container class="text-center">
    <v-row class="athlets-card-profile">
      <v-card
        color="#bef264"
        class="athlets-card"
        prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg"
        variant="tonal"
        rounded="xl"
        border="accent xl"
        width="500px"
        min-height="140"
      >
        <!-- TITLE -->
        <template #title>
          <span style="color: #aad95c"> Training Goal </span>
        </template>

        <!-- SUBTITLE -->
        <template #subtitle>
          <div class="subtitle-wrapper text-wrap" style="color: #87ac55">
            Set your goal race and training preferences
          </div>
        </template>
      </v-card>
    </v-row>

    <v-row class="choosing-fields">
      <v-col sm="4">
        <div
          style="
            text-align: left;
            margin-bottom: 4px;
            font-weight: 500;
            color: #bef264;
          "
        >
          Goal Race Distance
        </div>
        <v-select
          bg-color="#87ac55"
          active-color="#bef264"
          ref="Goal Race Distance"
          v-model="goal.raceDistance"
          :items="raceDistanceOptions"
          :rules="[() => !!raceDistanceOptions || 'This field is required']"
          class="mb-4"
          label="Goal Race Distance"
          placeholder="e.g., 5K, 10K, Half Marathon, Marathon"
          color="#293344"
          rounded="xl"
          hide-details
          clearable
          variant="solo-filled"
          :list-props="{ bgColor: '#bef264' }"
        ></v-select>
        <div
          style="
            text-align: left;
            margin-bottom: 4px;
            font-weight: 500;
            color: #bef264;
          "
        >
          Goal Time
        </div>
        <v-text-field
          v-model="goal.goalTime"
          label="Goal Time"
          variant="solo-filled"
          class="mb-4"
          placeholder="Enter time in minutes (14-300)"
          color="#293344"
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
          rounded="xl"
          bg-color="#87ac55"
        ></v-text-field>

        <div
          style="
            text-align: left;
            margin-bottom: 4px;
            font-weight: 500;
            color: #bef264;
          "
        >
          Personal Best
        </div>
        <v-text-field
          v-model="goal.personalBest"
          label="Personal Best"
          variant="solo-filled"
          class="mb-4"
          placeholder="Enter time in minutes (20-300)"
          color="#293344"
          type="text"
          min="14"
          max="300"
          :rules="[
            (v) => !!v || 'This field is required',
            (v) => /^[0-9]+$/.test(v) || 'Only numbers are allowed',
            (v) =>
              (parseInt(v) >= 14 && parseInt(v) <= 300) ||
              'Goal Time must be between 14 and 200 minutes',
          ]"
          clearable
          rounded="xl"
          bg-color="#87ac55"
        ></v-text-field>
        <div
          style="
            text-align: left;
            margin-bottom: 4px;
            font-weight: 500;
            color: #bef264;
          "
        >
          Target Race Date
        </div>
        <v-text-field
          type="date"
          bg-color="#87ac55"
          active-color="#bef264"
          :model-value="
            goal.targetDate ? goal.targetDate.toISOString().slice(0, 10) : ''
          "
          rounded="xl"
          clearable
          @update:model-value="
            (val) => {
              if (val) goal.targetDate = new Date(val);
              else goal.targetDate = null;
            }
          "
          variant="solo-filled"
          class="mb-4"
          label="Select Target Date (DD-MM-YYYY)"
          color="#293344"
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
        ></v-text-field>

        <div
          style="
            text-align: left;
            margin-bottom: 4px;
            font-weight: 500;
            color: #bef264;
          "
        >
          Training Days Per Week
        </div>
        <v-select
          bg-color="#87ac55"
          active-color="#bef264"
          label="Training Days Per Week "
          v-model="goal.trainingDays"
          :items="allowedTrainingDays"
          :rules="[(v) => !!v || 'This field is required']"
          v
          class="mb-4"
          placeholder="e.g., 3 days"
          color="#293344"
          rounded="xl"
          clearable
          variant="solo-filled"
          :list-props="{ bgColor: '#bef264' }"
        ></v-select>

        <div class="d-flex justify-space-between">
          <v-btn
            color="#bef264"
            class="mt-5"
            rounded
            elevation="16"
            @click="$router.back()"
          >
            <v-icon size="20">{{ icons.Left }}</v-icon
            >Back
          </v-btn>
          <v-btn
            color="#bef264"
            class="mt-5"
            rounded
            elevation="16"
            @click="goNext()"
            >Review <v-icon size="20">{{ icons.Right }}</v-icon></v-btn
          >
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
<script setup lang="ts">
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { computed } from "vue";
import "../assets/global.css";
import BaseCard from "../components/BaseCard.vue";
import { mdiChevronLeft, mdiChevronRight } from "@mdi/js";
import { useHead } from '@vueuse/head'

useHead({
  title: 'RunPlan – Set Your Training Goals',
  meta: [
    {
      name: 'description',
      content: 'Define your running goals, distances, and schedule to get a plan tailored to your objectives.'
    },
    { name: 'robots', content: 'index, follow' }
  ]
})

const store = useRunnerProfileStore();
const { goal } = storeToRefs(store);
const { profile } = storeToRefs(store);
const router = useRouter();

const icons = {
  Left: mdiChevronLeft,
  Right: mdiChevronRight,
};

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
