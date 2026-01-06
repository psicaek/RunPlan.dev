<template>
  <v-app class="gradient-bg">
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
          <v-btn color="primary" @click="goBack">Back</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { useRunnerProfileStore } from "../stores/useRunnerProfileStore";
import { useRouter } from "vue-router";
import { storeToRefs } from "pinia";

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

<style scoped>
.gradient-bg {
  background: linear-gradient(to bottom, #00b4db, #001f3f);
  min-height: 100vh;
}
.phase-endurance {
  color: #4caf50;
}
.phase-speed {
  color: #f44336;
}
.phase-taper {
  color: #2196f3;
}
</style>
