<template>
  <BaseCard></BaseCard>

  <v-container width="800px" style="justify-content: space-between">
    <v-card class="result-card">
      <v-row style="display: flex" justify="center">
        <v-card
          class="athlets-card"
          elevation="14"
          rounded="xl"
          style="margin-top: 30px"
          color="#1e293b"
          width="400px"
        >
          <!-- TITLE -->
          <template #title>
            <span style="font-weight: bolder"> Athletes Profile </span>
          </template>

          <!-- SUBTITLE -->
          <template #subtitle>
            <span style="color: #87ac55">
              Check if all Information is Correct.
            </span>
          </template>
        </v-card>
      </v-row>

      <v-row>
        <v-col align="center">
          <v-list-item class="review">
            <template #title> Experience Level: </template>
            <template #subtitle>
              <span class="profile-subtitle">
                {{ profile.experienceLevel || "-" }}
              </span>
            </template>
          </v-list-item>

          <v-list-item class="review">
            <template #title> Max Weekly Distance now: </template>
            <template #subtitle>
              <span class="profile-subtitle">
                {{
                  profile.weeklyDistance ? profile.weeklyDistance + " km" : "-"
                }}
              </span>
            </template>
          </v-list-item>

          <v-list-item class="review">
            <template #title> Longest Run ever: </template>
            <template #subtitle>
              <span>
                {{ profile.longestRun ? profile.longestRun + " km" : "-" }}
              </span>
            </template>
          </v-list-item>

          <v-list-item>
            <template #title> Age: </template>
            <template #subtitle>
              <span class="profile-subtitle">
                {{ profile.age || "-" }}
              </span>
            </template>
          </v-list-item>

          <v-list-item class="review">
            <template #title> Gender: </template>
            <template #subtitle>
              <span class="profile-subtitle">
                {{ profile.gender || "-" }}
              </span>
            </template>
          </v-list-item>
        </v-col>
      </v-row>
    </v-card>
    <v-divider class="devider"></v-divider>
    <v-card class="result-card" elevation="14">
      <v-row style="display: flex" justify="center">
        <v-row style="display: flex" justify="center">
          <v-card
            class="athlets-card"
            elevation="14"
            rounded="xl"
            style="margin-top: 45px"
            color="#1e293b"
            width="400px"
          >
            <!-- TITLE -->
            <template #title>
              <span style="font-weight: bolder"> Training Goal </span>
            </template>

            <!-- SUBTITLE -->
            <template #subtitle>
              <span style="color: #87ac55">
                Check if all Information is Correct.
              </span>
            </template>
          </v-card>
        </v-row>
      </v-row>
      <v-col align="center" style="margin-top: 25px">
        <v-list-item class="review">
          <
          <v-list-item-title>Race Distance:</v-list-item-title>
          <v-list-item-subtitle>{{
            goal.raceDistance || "-"
          }}</v-list-item-subtitle>
        </v-list-item>

        <v-list-item class="review">
          <v-list-item-title>Goal Time:</v-list-item-title>
          <v-list-item-subtitle
            >{{ goal.goalTime }} minutes</v-list-item-subtitle
          >
        </v-list-item>
        <v-list-item class="review">
          <v-list-item-title>Personal Best:</v-list-item-title>
          <v-list-item-subtitle
            >{{ goal.personalBest }} minutes</v-list-item-subtitle
          >
        </v-list-item>

        <v-list-item class="review">
          <v-list-item-title>Target Date:</v-list-item-title>
          <v-list-item-subtitle>{{ formattedTargetDate }}</v-list-item-subtitle>
        </v-list-item>

        <v-list-item class="review">
          <v-list-item-title>Training Days Per Week:</v-list-item-title>
          <v-list-item-subtitle>{{
            goal.trainingDays || "-"
          }}</v-list-item-subtitle>
        </v-list-item>
      </v-col>
    </v-card>
    <div class="d-flex justify-space-between">
      <v-btn
        color="#bef264"
        class="mt-5"
        rounded
        elevation="16"
        @click="$router.back()"
      >
        <v-icon size="20">mdi-arrow-left-box</v-icon>Back
      </v-btn>
      <v-btn
        color="#bef264"
        class="mt-5"
        rounded
        elevation="16"
        @click="generatePlan()"
        >Review
        <v-icon size="20" color="#001f3f">mdi-arrow-right-box</v-icon></v-btn
      >
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { computed } from "vue";
import "../assets/global.css";
import BaseCard from "../components/BaseCard.vue";

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

async function generatePlan() {
  try {
    const planData = await store.generateTrainingPlan(); // wait for backend
    // optional: you can do additional setup here if needed
    router.push("/result"); // navigate AFTER plan is ready
  } catch (err) {
    console.error("Error generating plan", err);
  }
}
</script>
