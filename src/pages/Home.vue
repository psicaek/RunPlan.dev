<template>
  <BaseCard></BaseCard>
  <!-- Hero Section -->
  <v-container fluid class="d-flex align-center justify-center home-container">
    <v-row class="justify-center">
      <v-col cols="12" sm="10" md="8" lg="6">
        <v-card
          variant="tonal"
          color="#bef264"
          class="pa-15 text-center hero-card"
          rounded="pill"
          border="accent xl"
        >
          <v-img
            src="/mainLogo.svg"
            alt="Run Plan Logo"
            max-width="120"
            class="mx-auto mb-7"
          />

          <h1 class="hero-title mb-3">Run Plan Generator</h1>

          <p class="hero-subtitle mb-4">
            Answer a few simple questions and get a running plan tailored to
            your goals.
          </p>

          <v-btn
            color="#BEF264"
            size="large"
            rounded="xl"
            elevation="24"
            @click="$router.push('/athletsProfile')"
          >
            Get Started
            <v-icon class="ml-1" color="bg-dark-900">
              mdi-arrow-right-box
            </v-icon>
          </v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
  <DonateCard></DonateCard>
</template>

<script setup>
import "../assets/global.css";
import BaseCard from "../components/BaseCard.vue";
import DonateCard from "../components/DonateCard.vue";
</script>
