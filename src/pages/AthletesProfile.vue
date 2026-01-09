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

    <!-- Title & Subtitle -->

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
            <span> Athletes Profile </span>
          </template>

          <!-- SUBTITLE -->
          <template #subtitle>
            <span style="color: #001f3f">
              Tell us about your current running level and experience.
            </span>
          </template>
        </v-card>
      </v-row>

      <v-row class="choosing-fields">
        <v-col sm="4">
          <div style="text-align: left; margin-bottom: 4px; font-weight: 500">
            Experience Level
          </div>
          <v-select
            ref="Experience Level"
            v-model="profile.experienceLevel"
            :items="experienceLevelOptions"
            :rules="[(v) => !!v || 'This field is required']"
            class="mb-4"
            placeholder="e.g., Beginner, Intermediate, Advanced"
            color="blue"
            :list-props="{ bgColor: '#001f3f' }"
          ></v-select>

          <div style="text-align: left; margin-bottom: 4px; font-weight: 500">
            Weekly Running Distance
          </div>
          <v-text-field
            v-model="profile.weeklyDistance"
            label="Weekly Running Distance"
            ref="weeklyDistanceInputRef"
            variant="outlined"
            class="mb-4"
            :rules="[weeklyDistanceRule]"
            placeholder="e.g., 10 km"
            color="#001f3f"
            suffix="km"
            :disabled="!profile.experienceLevel"
          ></v-text-field>
          <div style="text-align: left; margin-bottom: 4px; font-weight: 500">
            Longest Run Distance
          </div>
          <v-text-field
            v-model="profile.longestRun"
            label="Longest Run Distance"
            variant="outlined"
            class="mb-4"
            :rules="[
              (v) => !!v || 'This field is required',
              (v) => /^[0-9]+$/.test(v) || 'Only numbers are allowed',
              (v) =>
                (parseInt(v) >= 5 && parseInt(v) <= 42) ||
                'Distance must be between 5 and 42',
            ]"
            placeholder="e.g., 10 km"
            color="#001f3f"
            suffix="km"
          ></v-text-field>
          <div style="text-align: left; margin-bottom: 4px; font-weight: 500">
            Age
          </div>
          <v-text-field
            v-model="profile.age"
            label="Age"
            variant="outlined"
            class="mb-4"
            :rules="[
              (v) => !!v || 'This field is required',
              (v) => /^[0-9]+$/.test(v) || 'Only numbers are allowed',
              (v) =>
                (parseInt(v) >= 12 && parseInt(v) <= 65) ||
                'Age must be between 12 and 65',
            ]"
            placeholder="e.g., 25"
            color="#001f3f"
          ></v-text-field>
          <div style="text-align: left; margin-bottom: 4px; font-weight: 500">
            Gender
          </div>
          <v-select
            ref="Gender"
            v-model="profile.gender"
            :items="genderOptions"
            :rules="[() => !!profile.gender || 'This field is required']"
            label="Gender"
            placeholder="Select..."
            required
            color="#001f3f"
            :list-props="{ bgColor: '#001f3f' }"
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
              >Next <v-icon size="20">mdi-arrow-right-box</v-icon></v-btn
            >
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script setup lang="ts">
import { ref, computed, watch } from "vue";
import { useRouter } from "vue-router";
import { storeToRefs } from "pinia";
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import "../assets/global.css";

// Pinia store
const store = useRunnerProfileStore();
const { profile } = storeToRefs(store);

const router = useRouter();

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
  }
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
