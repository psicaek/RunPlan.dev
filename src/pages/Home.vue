<template>
  <v-main class="gradient-bg">
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
    <!-- Hero Section -->
    <v-container fluid class="fill-height">
      <v-row align="center" justify="center" class="text-center">
        <v-col cols="12" md="8" lg="6">
          <!-- Logo -->
          <v-img
            src="src/assets/mainLogo.svg"
            alt="Run Plan Logo"
            width="160"
            class="mx-auto mb-6"
          />

          <!-- Title -->
          <h1 class="text-h2 font-weight-bold mb-4">Run Plan Generator</h1>

          <!-- Subtitle -->
          <p class="text-h6 mb-8">
            Answer a few simple questions and get a running plan tailored to
            your goals.
          </p>

          <!-- Button -->
          <v-btn
            color="#001f3f"
            size="x-large"
            rounded="xl"
            elevation="24"
            @click="$router.push('/athletsProfile')"
          >
            Get Started
            <v-icon class="ml-2">mdi-arrow-right-box</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import "../assets/global.css";
export default {
  name: "HomePage",
};
</script>
