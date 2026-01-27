<template>
  <BaseCard></BaseCard>

  <v-container class="text-center">
    <v-row class="athlets-card-profile">
      <v-card
        color="#bef264"
        class="athlets-card"
        prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg"
        variant="tonal"
        rounded="xl"
        border="accent xl"
        width="700px"
        height="125px"
      >
        <!-- TITLE -->
        <template #title>
          <span style="color: #aad95c"> Athlete Profile </span>
        </template>

        <!-- SUBTITLE -->
        <template #subtitle>
          <span style="color: #87ac55"> Field Descriptions </span>
        </template>
      </v-card>
    </v-row>
  </v-container>

  <v-row class="text-center">
    <v-col cols="12" md="6" class="pa-2">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Experience Level"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            Choose the level that best represents your current running
            background
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            Your experience level helps determine how much training load your
            body can safely handle. Each level corresponds to a typical weekly
            running distance. Beginners usually run 5–15 km per week,
            intermediates 10–25 km, and advanced runners 20–50 km with
            structured training. Expert runners handle higher volumes of 40–80
            km weekly, while elite runners train competitively with 70–150 km
            per week. Choosing the correct level ensures safe progression and
            helps reduce injury risk..
          </span>
        </template></v-card
      >
    </v-col>

    <v-col cols="12" md="6" class="pa-2">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Weekly Running Distance"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            Your current weekly training volume
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            The total distance you ran in your most recent training week. This
            value helps determine your aerobic base, recovery capacity, and how
            much training load your body is used to handling safely.
          </span>
        </template>
      </v-card>
    </v-col>

    <v-col class="text-center">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Longest Running Distance"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            Your maximum endurance achievement
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            The longest distance you have ever run in a single session. This is
            used to safely prescribe long runs and prevent excessive jumps in
            distance that could increase injury risk.</span
          >
        </template></v-card
      >
    </v-col>
  </v-row>
  <v-row class="text-center" style="margin-bottom: 35px">
    <v-col cols="12" md="6" class="pa-2">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Age"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            Used for training intensity adjustments
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            Age helps fine-tune recovery time, pacing ranges, and intensity
            zones. As age increases, recovery becomes more important, and
            training stress is adjusted accordingly to maintain progress and
            reduce injury risk.
          </span>
        </template></v-card
      >
    </v-col>

    <v-col cols="12" md="6" class="pa-2">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Gender"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            Physiological reference for training calculations
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            Gender is used as a reference for physiological differences such as
            average heart rate response, recovery patterns, and performance
            modeling. It helps personalize pacing and effort recommendations
            more accurately.
          </span>
        </template></v-card
      >
    </v-col>
  </v-row>
  <v-divider
    :thickness="15"
    class="border-opacity-100"
    color="#bef264"
  ></v-divider>
  <v-container class="text-center">
    <v-row class="athlets-card-profile">
      <v-card
        color="#bef264"
        class="athlets-card"
        prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg"
        variant="tonal"
        rounded="xl"
        border="accent xl"
        width="700px"
        height="125px"
      >
        <!-- TITLE -->
        <template #title>
          <span style="color: #aad95c"> Training Goal </span>
        </template>

        <!-- SUBTITLE -->
        <template #subtitle>
          <span style="color: #87ac55"> Field Descriptions </span>
        </template>
      </v-card>
    </v-row>
  </v-container>

  <v-row class="text-center">
    <v-col cols="12" md="6" class="pa-2">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Goal Race Distance"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            The race you are training for
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            Defines the target event distance (e.g. 5K, 10K, Half Marathon).
            This choice shapes the entire training plan, including workout
            types, long run length, and pacing strategy.
          </span>
        </template></v-card
      >
    </v-col>

    <v-col cols="12" md="6" class="pa-2">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Goal Time"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            Your desired finish time
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            Represents the performance goal for race day. It is used to
            calculate training paces and intensity zones, ensuring workouts
            match your target performance.
          </span>
        </template>
      </v-card>
    </v-col>

    <v-col class="text-center">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Personal Best"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            Your fastest previous performance
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            Shows your best completed race time for the selected distance. This
            helps estimate your current fitness level and keeps training targets
            realistic and safe.</span
          >
        </template></v-card
      >
    </v-col>
  </v-row>
  <v-row class="text-center">
    <v-col cols="12" md="6" class="pa-2">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Target Race Date"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            When your goal race takes place
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            Sets the training timeline by defining how many weeks are available
            for preparation, progression, and tapering before race day.
          </span>
        </template></v-card
      >
    </v-col>

    <v-col cols="12" md="6" class="pa-2" style="margin-bottom: 20px">
      <v-card
        color="#bef264"
        variant="tonal"
        border="accent xl"
        rounded="xl"
        class="infocard"
        title="Training Days per Week"
      >
        <template #subtitle>
          <span class="info-card .v-card-subtitle">
            How often you plan to train
          </span>
        </template>
        <template #text>
          <span class="info-card .v-card-subtitle" style="font-size: medium">
            Indicates the number of days you will run each week. This helps
            balance training load and recovery while fitting the plan into your
            schedule.
          </span>
        </template></v-card
      >
    </v-col>
  </v-row>
  <v-row justify="center" class="mt-8">
    <v-btn
      color="#bef264"
      rounded
      elevation="12"
      style="margin-bottom: 20px"
      @click="$router.back()"
    >
      <v-icon start>{{ mdiChevronLeft }}</v-icon>
      Back
    </v-btn>
  </v-row>
  <DonateCard style="margin-top: 20px"></DonateCard>
</template>
<script setup lang="ts">
import "../assets/global.css";
import BaseCard from "../components/BaseCard.vue";
import DonateCard from "../components/DonateCard.vue";
import { mdiChevronLeft } from "@mdi/js";
</script>
