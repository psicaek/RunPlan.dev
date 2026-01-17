<template>
  <BaseCard></BaseCard>
  <!-- Hero Section -->
  <v-container fluid class="fill-height">
    <v-card
      variant="tonal"
      style="margin: auto"
      color="#bef264"
      width="1000px"
      height="480px"
      rounded="pill"
      border="accent xl"
    >
      <v-row
        align="center"
        justify="center"
        class="text-center"
        style="margin-top: 25px"
      >
        <v-col lg="7">
          <!-- Logo -->
          <v-img
            src="/mainLogo.svg"
            alt="Run Plan Logo"
            width="160"
            class="mx-auto mb-6"
          />

          <!-- Title -->
          <h1 class="text-h2 font-weight-bold mb-1">Run Plan Generator</h1>
          <v-card-text style="color: #87ac55">
            <!-- Subtitle -->
            <h2 class="text-h6 font-weight-bold mb-1">
              Answer a few simple questions and get a running plan tailored to
              your goals.
            </h2>
          </v-card-text>
          <!-- Button -->
          <v-btn
            color="#BEF264"
            size="x-large"
            rounded="xl"
            elevation="24"
            @click="$router.push('/athletsProfile')"
          >
            Get Started
            <v-icon class="ml-2" color="bg-dark-900"
              >mdi-arrow-right-box</v-icon
            >
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script setup>
import "../assets/global.css";
import BaseCard from "../components/BaseCard.vue";
</script>
