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
            <p class="page-title-text">Athlete Profile</p>
            <p class="page-second-text">
              Tell us about your current running level and experience.
            </p>
          </v-col>
        </v-row>
      </v-container>
      <v-container class="text-center">
        <v-card-text>
          <v-row justify="center">
            <v-col cols="12" sm="6">
              <div
                style="text-align: left; margin-bottom: 4px; font-weight: 500"
              >
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
              ></v-select>
              <div
                style="text-align: left; margin-bottom: 4px; font-weight: 500"
              >
                Weekly Running Distance
              </div>
              <v-text-field
                v-model="profile.weeklyDistance"
                label="Weekly Running Distance"
                variant="outlined"
                class="mb-4"
                :rules="[
                  (v) => !!v || 'This field is required',
                  (v) => /^[0-9]+$/.test(v) || 'Only numbers are allowed',
                  (v) =>
                    (parseInt(v) >= 20 && parseInt(v) <= 200) ||
                    'Longest Weekly Distance must be between 20 and 200',
                ]"
                placeholder="e.g., 10 km"
                color="blue"
                suffix="km"
              ></v-text-field>
              <div
                style="text-align: left; margin-bottom: 4px; font-weight: 500"
              >
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
                color="blue"
                suffix="km"
              ></v-text-field>
              <div
                style="text-align: left; margin-bottom: 4px; font-weight: 500"
              >
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
                color="blue"
              ></v-text-field>
              <div
                style="text-align: left; margin-bottom: 4px; font-weight: 500"
              >
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
                color="blue"
              ></v-select>
              <v-btn color="primary" class="mt-5" @click="$router.back()"
                >Back
              </v-btn>
              <v-btn color="success" class="mt-5" @click="goNext()">
                Next
              </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

const router = useRouter();

const store = useRunnerProfileStore();
const { profile } = storeToRefs(store);
const experienceLevelOptions = [
  "Beginner",
  "Intermediate",
  "Advance",
  "Expert",
  "Elite",
];
const genderOptions = ["Male", "Female"];

function goNext() {
  if (store.isProfileComplete()) {
    router.push({ name: "TrainingGoal" });
    console.log("next page ");
  } else {
    alert("Please complete all fields.");
    console.log("something is wrong ");
  }
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
.text-left {
  text-align: left;
}
</style>
