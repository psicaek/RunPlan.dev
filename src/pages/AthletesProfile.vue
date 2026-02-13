<template>
  <BaseCard></BaseCard>

  <!-- Title & Subtitle -->

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
          <span style="color: #aad95c"> Athletes Profile </span>
        </template>

        <!-- SUBTITLE -->
        <template #subtitle>
          <span class="subtitle-wrapper text-wrap" style="color: #87ac55">
            Tell us about your current running level and experience.
          </span>
        </template>
      </v-card>
    </v-row>

    <v-row class="choosing-fields">
      <v-col sm="4">
        <div style="text-align: left; color: #bef264">Experience Level</div>
        <v-select
          bg-color="#87ac55"
          active-color="#bef264"
          ref="Experience Level"
          v-model="profile.experienceLevel"
          :items="experienceLevelOptions"
          :rules="[(v) => !!v || 'This field is required']"
          class="mb-4"
          label="Experience level"
          placeholder="e.g., 5K, 10K, Half Marathon, Marathon"
          color="#293344"
          :list-props="{ bgColor: '#bef264' }"
          rounded="xl"
          clearable
          variant="solo-filled"
        ></v-select>

        <div
          style="
            text-align: left;
            margin-bottom: 4px;
            font-weight: 500;
            color: #bef264;
          "
        >
          Weekly Running Distance
        </div>
        <v-text-field
          v-model="profile.weeklyDistance"
          label="Weekly Running Distance"
          ref="weeklyDistanceInputRef"
          variant="solo-filled"
          class="mb-4"
          :rules="[weeklyDistanceRule]"
          placeholder="e.g., 10 km"
          suffix="km"
          :disabled="!profile.experienceLevel"
          rounded="xl"
          clearable
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
          Longest Run Distance
        </div>
        <v-text-field
          v-model="profile.longestRun"
          label="Longest Run Distance"
          variant="solo-filled"
          class="mb-4"
          :rules="[
            (v) => !!v || 'This field is required',
            (v) => /^[0-9]+$/.test(v) || 'Only numbers are allowed',
            (v) =>
              (parseInt(v) >= 5 && parseInt(v) <= 42) ||
              'Distance must be between 5 and 42',
          ]"
          placeholder="e.g., 10 km"
          suffix="km"
          rounded="xl"
          clearable
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
          Age
        </div>
        <v-text-field
          v-model="profile.age"
          label="Age"
          variant="solo-filled"
          class="mb-4"
          :rules="[
            (v) => !!v || 'This field is required',
            (v) => /^[0-9]+$/.test(v) || 'Only numbers are allowed',
            (v) =>
              (parseInt(v) >= 12 && parseInt(v) <= 65) ||
              'Age must be between 12 and 65',
          ]"
          placeholder="e.g., 25"
          rounded="xl"
          clearable
          bg-color="#87ac55"
          base-color="#87ac55"
        ></v-text-field>
        <div
          style="
            text-align: left;
            margin-bottom: 4px;
            font-weight: 500;
            color: #bef264;
          "
        >
          Gender
        </div>
        <v-select
          bg-color="#87ac55"
          ref="Gender"
          v-model="profile.gender"
          :items="genderOptions"
          :rules="[() => !!profile.gender || 'This field is required']"
          label="Gender"
          placeholder="Select..."
          required
          :list-props="{ bgColor: '#bef264' }"
          rounded="xl"
          clearable
          variant="solo-filled"
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
            >Next <v-icon size="20">{{ icons.Right }}</v-icon></v-btn
          >
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref, computed, watch } from "vue";
import { useRouter } from "vue-router";
import { storeToRefs } from "pinia";
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import "../assets/global.css";
import BaseCard from "../components/BaseCard.vue";
import { mdiChevronLeft, mdiChevronRight } from "@mdi/js";
import { useHead } from '@vueuse/head'

useHead({
  title: 'RunPlan – Create Your Athlete Profile',
  meta: [
    {
      name: 'description',
      content: 'Enter your running experience, fitness level, and preferences to generate a personalized training plan.'
    },
    { name: 'robots', content: 'index, follow' }
  ]
})

// Pinia store
const store = useRunnerProfileStore();
const { profile } = storeToRefs(store);

const router = useRouter();

const icons = {
  Left: mdiChevronLeft,
  Right: mdiChevronRight,
};

// Refs
const weeklyDistanceInputRef = ref();

// Experience levels
const experienceLevelOptions = [
  "Beginner",
  "Intermediate",
  "Advanced",
  "Expert",
  "Elite",
];

// Gender
const genderOptions = ["Male", "Female"];

// Weekly distance ranges per experience level
const weeklyDistanceRanges: Record<string, [number, number]> = {
  Beginner: [5, 15],
  Intermediate: [10, 25],
  Advanced: [20, 50],
  Expert: [40, 80],
  Elite: [70, 150],
};

// Validation rule for weekly distance
const weeklyDistanceRule = computed(() => {
  return (v: string | number) => {
    if (v === null || v === undefined || v === "")
      return "This field is required";

    const value = parseInt(String(v));
    const level = profile.value.experienceLevel;

    if (!level) return "Select experience level first";

    const [min, max] =
      weeklyDistanceRanges[level as keyof typeof weeklyDistanceRanges];
    return value >= min && value <= max
      ? true
      : `Weekly distance for ${level} must be between ${min} and ${max} km`;
  };
});

// Watch experience level to reset/validate weekly distance
watch(
  () => profile.value.experienceLevel,
  () => {
    const level = profile.value.experienceLevel;
    if (!level) return;

    const [min, max] =
      weeklyDistanceRanges[level as keyof typeof weeklyDistanceRanges];

    // Reset weekly distance if out of new range
    if (
      profile.value.weeklyDistance !== null &&
      profile.value.weeklyDistance !== undefined &&
      (profile.value.weeklyDistance < min || profile.value.weeklyDistance > max)
    ) {
      profile.value.weeklyDistance = null;
    }

    // Force Vuetify validation
    if (weeklyDistanceInputRef.value?.validate) {
      weeklyDistanceInputRef.value.validate(true);
    }
  },
);

// Navigation
function goNext() {
  if (store.isProfileComplete()) {
    router.push({ name: "TrainingGoal" });
  } else {
    alert("Please complete all fields.");
  }
}
</script>
