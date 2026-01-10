<template>
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
  <v-container>
    <h2 class="text-h4 font-weight-bold mb-6">🏁 Your Training Plan</h2>

    <v-alert
      v-if="!plan || !plan.weeks || plan.weeks.length === 0"
      type="info"
      class="mb-4"
    >
      No plan generated yet.
    </v-alert>

    <v-card
      v-for="week in plan.weeks"
      :key="week.week"
      class="mb-4"
      elevation="3"
    >
      <v-card-title>
        Week {{ week.week }} — Total {{ week.total_km }} km
      </v-card-title>

      <v-divider></v-divider>

      <v-card-text>
        <v-list dense>
          <v-list-item v-for="(run, index) in week.runs" :key="index">
            <v-list-item-title>
              {{ run.type.toUpperCase() }} — {{ run.distance }} km
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>

    <v-row justify="center" class="mt-10">
      <v-col cols="auto">
        <v-btn color="primary" @click="goBack()">Back</v-btn>
      </v-col>
    </v-row>
  </v-container>
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

onMounted(() => {
  if (plan.value) {
    store.generateTrainingPlan();
  }
});

function goBack() {
  router.back();
}
</script>
