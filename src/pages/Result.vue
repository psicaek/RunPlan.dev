<template>
  <v-app class="gradient-bg">
    <v-container>
      <h2 class="text-h4 font-weight-bold mb-6">🏁 Your Training Plan</h2>

      <v-alert v-if="!plan || plan.length === 0" type="info" class="mb-4">
        No plan generated yet.
      </v-alert>

      <v-card v-for="week in plan" :key="week.week" class="mb-4" elevation="3">
        <v-card-title
          >Week {{ week.week }} Total KM {{ week.weekKm }}</v-card-title
        >
        <v-divider></v-divider>
        <v-card-text>
          <v-list dense>
            <v-list-item v-for="(day, i) in week.days" :key="i">
              <v-list-item-content>
                <v-list-item-title>
                  {{ day.day }} – {{ day.type }}: {{ day.distance }} km
                </v-list-item-title>
                <v-list-item-subtitle
                  >Pace: {{ day.pace }}</v-list-item-subtitle
                >
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
      <v-row justify="center" class="mt-10">
        <v-col cols="auto">
          <v-btn color="primary" @click="goBack">Back</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup>
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import { useRouter } from "vue-router";

const router = useRouter();

const store = useRunnerProfileStore();
const plan = store.trainingPlan;

function goBack() {
  router.back();
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
