<template>
  <v-card class="result-card mt-6" elevation="14">
    <v-row justify="center">
      <v-card
        class="athlets-card"
        elevation="14"
        rounded="xl"
        color="#1e293b"
        width="400px"
      >
        <template #title>
          <span style="font-weight: bolder"> Training Plan </span>
        </template>
        <template #subtitle>
          <span style="color: #87ac55"> Weekly runs with pace per type </span>
        </template>
      </v-card>
    </v-row>

    <v-container>
      <v-expansion-panels>
        <v-expansion-panel v-for="week in plan.weeks" :key="week.week">
          <v-expansion-panel-title>
            Week {{ week.week }} — {{ week.total_km }} km
          </v-expansion-panel-title>

          <v-expansion-panel-text>
            <v-list density="compact">
              <v-list-item v-for="(run, index) in week.runs" :key="index">
                <v-list-item-title>
                  {{ run.type.toUpperCase() }} —
                  {{ getDistance(run.distance) }} km
                </v-list-item-title>

                <v-list-item-subtitle>
                  Pace: {{ run.pace_per_run_type }} /km
                </v-list-item-subtitle>
              </v-list-item>
            </v-list>
          </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </v-card>

  <v-row justify="center" class="mt-10">
    <v-col cols="auto">
      <v-btn color="primary" @click="goBack()">Back</v-btn>
    </v-col>
  </v-row>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import { useRouter } from "vue-router";
import { storeToRefs } from "pinia";
import "../assets/global.css";

const router = useRouter();
const store = useRunnerProfileStore();
const { trainingPlan: plan, isGenerating } = storeToRefs(store); // 👈 Αυτό είναι το σωστό reactive binding
const getDistance = (distance) => {
  return typeof distance === "object" ? distance.parsedValue : distance;
};

onMounted(() => {
  if (!plan.value) {
    store.generateTrainingPlan();
  }
});

function goBack() {
  router.back();
}
</script>
