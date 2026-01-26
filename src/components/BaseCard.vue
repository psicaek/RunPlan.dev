<template>
  <v-card class="rounded-0">
    <!-- Title with icons -->
    <span class="title-runplan text-h">
      <v-icon size="40">{{ icons.Run }}</v-icon>
      <span
        style="
          font-family: &quot;Montserrat&quot;, sans-serif;
          font-weight: 700;
        "
        >Run Plan Generator</span
      >
      <v-icon size="40">{{ icons.Runfast }}</v-icon>
    </span>
    <!-- Subtitle under the title -->
    <span
      class="title-runplan2"
      style="
        text-align: center;
        font-family: &quot;Montserrat&quot;, sans-serif;
        font-weight: 500;
      "
    >
      Create your personalized running plan in minutes!
    </span>
  </v-card>
</template>

<script setup lang="ts">
import "../assets/global.css";
import { mdiRun, mdiRunFast } from "@mdi/js";

const icons = {
  Run: mdiRun,
  Runfast: mdiRunFast,
};
</script>
