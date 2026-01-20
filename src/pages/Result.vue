<template>
  <BaseCard></BaseCard>
  <v-container class="text-center">
    <v-row class="athlets-card-profile">
      <v-card
        class="athlets-card"
        elevation="14"
        rounded="xl"
        color="#bef264"
        style="margin-top: 30px"
        width="500px"
        min-height="140"
        variant="tonal"
      >
        <template #title>
          <span style="font-weight: bolder"> Training Plan </span>
        </template>
        <template #subtitle>
          <span class="subtitle-wrapper text-wrap" style="color: #87ac55">
            Total Weeks {{ plan.weeks_until }} with type of Runs per Week:
            {{ plan.type_of_runs.join(", ") }}
          </span>
        </template>
      </v-card>
    </v-row>
    <div id="print-area">
      <v-container>
       
        <v-expansion-panels
        v-model="openPanels"
          color="#bef264"
          variant="popout"
          style="margin-top: 20px"
          multiple
        >
          <v-expansion-panel
        v-for="(week, index) in plan?.weeks || []"
        :key="week.week"
        :value="index"
        style="background-color: #87ac55"
        elevation="24"
      >
            <v-expansion-panel-title style="margin-top: 10px">
              Week {{ week.week }} — Weekly Total KM {{ week.total_km }} km
            </v-expansion-panel-title>

            <v-expansion-panel-text style="background-color: #1e293b">
              <v-list density="compact" style="background-color: #87ac55">
                <v-list-item v-for="(run, index) in week.runs" :key="index">
                  <v-list-item-title
                    class="cursor-pointer text-#87ac55 hover:underline"
                    @click="scrollToRun(run.type)"
                  >
                    {{ run.type.toUpperCase() }} —
                    {{ getDistance(run.distance) }} km
                  </v-list-item-title>

                  <v-list-item-subtitle>
                    Pace: {{ run.pace_per_run_type }} /km or Heartrate: {{ run.bpm }}
                  </v-list-item-subtitle>
                </v-list-item>
              </v-list>
            </v-expansion-panel-text>
          </v-expansion-panel>
        </v-expansion-panels>
        <v-col >
      <v-btn
        color="#bef264"
        class="mt-5"
        rounded
        elevation="16"
        @click="expandAll"
      >
        <v-icon size="20">{{ icons.expandAll}}</v-icon
        >Expand All
      </v-btn>
      <v-btn
        color="#bef264"
        class="mt-5"
        rounded
        elevation="16"
        @click="collapseAll"
      >
        <v-icon size="20">{{ icons.collapseAll }}</v-icon> Collapse All
      </v-btn>
    </v-col>
      </v-container>
    </div>
    <v-col class="d-flex justify-space-between">
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
        @click="printResult"
      >
        <v-icon size="20">{{ icons.Printer }}</v-icon> Print Plan
      </v-btn>
    </v-col>

    <v-row class="text-center">
      <v-col class="info-card">
        <v-card
          color="#bef264"
          variant="tonal"
          border="accent xl"
          rounded="xl"
          class="infocard"
          title="Easy Run"
          ref="Easyrun"
          ><v-card-text>
            <ul
              class="pl-4 list-disc text-sm"
              style="font-size: medium; text-align: start"
            >
              <li>Pace: ~60–75% of 10k pace (conversational pace)</li>
              <li>Heart Rate: 60–75% of max HR</li>
              <li>Effort: Very easy, can talk comfortably</li>
              <li>Purpose: Aerobic base, recovery, injury prevention</li>
              <li>
                Tips: Focus on relaxed form, keep shoulders loose, breathe
                naturally
              </li>
            </ul>
          </v-card-text>
          <template #subtitle>
            <span class="info-card .v-card-subtitle">
              Run at a comfortable pace. You should be able to hold a
              conversation.
            </span>
          </template>
        </v-card>
      </v-col>

      <v-col class="info-card">
        <v-card
          color="#bef264"
          variant="tonal"
          border="accent xl"
          rounded="xl"
          class="infocard"
          title="Interval / VO2max "
          ref="Interval"
        >
          <v-card-text>
            <ul
              class="pl-4 list-disc text-sm"
              style="font-size: medium; text-align: start"
            >
              <li>Pace: Faster than 10k pace</li>
              <li>Heart Rate: 90–100% of max HR</li>
              <li>High-intensity bursts, very hard</li>
              <li>Purpose: Improve VO2 max, speed, cardiovascular capacity</li>
              <li>
                Tips: Full recovery between intervals, maintain good form, don’t
                overdo volume
              </li>
            </ul>
          </v-card-text>
          <template #subtitle>
            <span class="info-card .v-card-subtitle">
              Fast, intense bursts. Heart rate very high, anaerobic effort.
              Builds speed, power, and cardiovascular fitness.
            </span>
          </template></v-card
        >
      </v-col>
    </v-row>
    <v-row>
      <v-col class="info-card">
        <v-card
          color="#bef264"
          variant="tonal"
          border="accent xl"
          rounded="xl"
          class="infocard"
          title="Long Run"
          ref="Longrun"
        >
          <v-card-text>
            <ul
              class="pl-4 list-disc text-sm"
              style="font-size: medium; text-align: start"
            >
              <li>
                Pace: Slightly slower than easy pace (~65–80% of 10k pace)
              </li>
              <li>Heart Rate: 65–80% of max HR</li>
              <li>Effort: Steady, moderate</li>
              <li>Purpose: Improve endurance, mental toughness, stamina</li>
              <li>
                Tips: Hydrate properly, practice nutrition, maintain even effort
              </li>
            </ul>
          </v-card-text>
          <template #subtitle>
            <span class="info-card .v-card-subtitle">
              Steady, endurance-focused, moderate effort. Builds stamina and
              aerobic capacity. Keep pace consistent, focus on breathing and
              form.
            </span>
          </template></v-card
        >
      </v-col>
      <v-col class="info-card">
        <v-card
          color="#bef264"
          variant="tonal"
          border="accent xl"
          rounded="xl"
          class="infocard"
          title="Recovery Run"
          ref="Recovery"
          ><v-card-text>
            <ul
              class="pl-4 list-disc text-sm"
              style="font-size: medium; text-align: start"
            >
              <li>Pace: ~60–75% of 10k pace (conversational pace)</li>
              <li>Heart Rate: 60–75% of max HR</li>
              <li>Effort: Very easy, can talk comfortably</li>
              <li>Purpose: Aerobic base, recovery, injury prevention</li>
              <li>
                Tips: Focus on relaxed form, keep shoulders loose, breathe
                naturally
              </li>
            </ul>
          </v-card-text>
          <template #subtitle>
            <span class="info-card .v-card-subtitle">
              Run at a comfortable pace. You should be able to hold a
              conversation.
            </span>
          </template>
        </v-card>
      </v-col>
      <v-col class="info-card">
        <v-card
          color="#bef264"
          variant="tonal"
          border="accent xl"
          rounded="xl"
          class="infocard"
          title="Tempo Run"
          ref="Tempo"
          ><v-card-text>
            <ul
              class="pl-4 list-disc text-sm"
              style="font-size: medium; text-align: start"
            >
              <li>Pace: ~10–20 seconds slower than 10k pace</li>
              <li>Heart Rate: 80–90% of max HR</li>
              <li>Effort: “Comfortably hard”, challenging but sustainable</li>
              <li>
                Purpose: Raise lactate threshold, improve race pace stamina
              </li>
              <li>
                Tips: Warm up thoroughly, maintain steady rhythm, focus on
                midfoot strike
              </li>
            </ul>
          </v-card-text>
          <template #subtitle>
            <span class="info-card .v-card-subtitle">
              Run at a comfortable pace. You should be able to hold a
              conversation.
            </span>
          </template>
        </v-card>
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
import BaseCard from "../components/BaseCard.vue";
import { ref } from "vue";
import { mdiChevronLeft, mdiPrinter ,mdiExpandAll, mdiCollapseAll} from "@mdi/js";

const router = useRouter();
const store = useRunnerProfileStore();
const { trainingPlan: plan, isGenerating } = storeToRefs(store); // 👈 Αυτό είναι το σωστό reactive binding
const getDistance = (distance) => {
  return typeof distance === "object" ? distance.parsedValue : distance;
};
const Easyrun = ref(null);
const Longrun = ref(null);
const Recovery = ref(null);
const Interval = ref(null);
const Tempo = ref(null);

const printResult = () => {
  window.print();
};

const icons = {
  Left: mdiChevronLeft,
  Printer: mdiPrinter,
  expandAll:mdiExpandAll,
  collapseAll:mdiCollapseAll
};

const openPanels = ref([])

const expandAll = () => {
  console.log('Expanding, weeks count:', plan.value.weeks.length)
  openPanels.value = plan.value.weeks.map((_, index) => index)
  console.log('Open panels:', openPanels.value)
}

const collapseAll = () => {
  openPanels.value = []
}

function scrollToRun(type) {
  const map = {
    easy: Easyrun,
    long: Longrun,
    recovery: Recovery,
    interval: Interval,
    tempo: Tempo,
  };

  map[type]?.value?.$el.scrollIntoView({
    behavior: "smooth",
    block: "start",
  });
}

onMounted(() => {
  if (!plan.value) {
    store.generateTrainingPlan();
  }
});

function goBack() {
  router.back();
}
</script>
<style>
@media print {
  body * {
    visibility: hidden;
  }

  #print-area,
  #print-area * {
    visibility: visible;
  }

  #print-area {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
  }
}
</style>
