<template>
  <v-app class="gradient-bg">
    <v-container>
      <h2 class="text-h4 font-weight-bold mb-6">🏁 Your Training Plan</h2>

      <!-- No plan -->
      <v-alert v-if="!plan" type="info" class="mb-4">
        No plan generated yet.
      </v-alert>

      <!-- Plan exists -->
      <div v-else>
        <!-- Summary -->
        <v-card class="mb-6" elevation="2">
          <v-card-text>
            <p><strong>Weeks until race:</strong> {{ plan.weeks_until }}</p>
            <p><strong>Target pace:</strong> {{ plan.pace }} min/km</p>
            <p>
              <strong>Training types:</strong>
              {{ plan.weekly_type_of_runs.join(", ") }}
            </p>
          </v-card-text>
        </v-card>

        <!-- Weekly cards -->
        <v-card
          v-for="(weekKm, index) in plan.weekly_mileage"
          :key="index"
          class="mb-4"
          elevation="3"
        >
          <v-card-title>
            Week {{ index + 1 }} — Total: {{ weekKm }} km
          </v-card-title>

          <v-divider />

          <v-card-text>
            <v-list dense>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>
                    🟢 Easy run: {{ plan.run_per_type[index].easy }} km
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    Pace: {{ plan.pace }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>

              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>
                    🔴 Interval run: {{ plan.run_per_type[index].interval }} km
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    Faster than {{ plan.pace }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>

              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>
                    🔵 Long run: {{ plan.run_per_type[index].long }} km
                  </v-list-item-title>
                  <v-list-item-subtitle> Easy pace </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>

              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>
                    🔵 Long run: {{ plan.run_per_type[index].long }} km
                  </v-list-item-title>
                  <v-list-item-subtitle> Easy pace </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </div>

      <!-- Back button -->
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
