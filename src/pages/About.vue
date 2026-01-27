<template>
  <BaseCard />

  <v-container class="mt-8" style="text-align: center">
    <v-row
      justify="center"
      class="mb-6"
      v-for="(section, index) in sections"
      :key="index"
    >
      <v-col cols="12" md="8">
        <v-card
          color="#bef264"
          variant="tonal"
          rounded="xl"
          class="pa-6"
          elevation="16"
        >
          <v-card-title class="text-h6 font-weight-bold">
            {{ section.title }}
          </v-card-title>
          <v-card-subtitle>
            {{ section.subtitle }}
          </v-card-subtitle>
          <v-card-text>
            {{ section.text }}
          </v-card-text>
          <!-- Optional buttons for support -->
          <v-card-actions style="display: block" v-if="section.supportLinks">
            <v-btn
              v-for="(link, i) in section.supportLinks"
              :key="i"
              :href="link.url"
              target="_blank"
              :color="link.color"
              class="ma-2"
              rounded
            >
              <v-icon left v-if="link.icon && !link.img">{{
                link.icon
              }}</v-icon>
              <img
                v-if="link.img"
                :src="link.img"
                alt="PayPal"
                style="width: 20px; height: 20px; margin-right: 6px"
              />
              {{ link.label }}
            </v-btn>
          </v-card-actions>
        </v-card>
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
  </v-container>
  <DonateCard></DonateCard>
</template>

<script setup lang="ts">
import BaseCard from "../components/BaseCard.vue";
import DonateCard from "../components/DonateCard.vue";
import { mdiChevronLeft } from "@mdi/js";
interface Section {
  title: string;
  subtitle: string;
  text: string;
  supportLinks?: {
    label: string;
    url: string;

    icon: string;
    color: string;
  }[];
}

const sections: Section[] = [
  {
    title: "About This App",
    subtitle: "Personalized running plans, built around you",
    text: "This application helps runners of all levels create personalized training plans based on their experience, goals, and availability. Each plan is designed to be realistic, safe, and easy to follow.",
  },
  {
    title: "Our Goal",
    subtitle: "Smart training without unnecessary complexity",
    text: "The goal is to make structured training accessible to everyone. Whether you are training for your first race or a new personal best, the focus is on consistency, progress, and long-term improvement.",
  },
  {
    title: "How It Works",
    subtitle: "Data-driven, runner-focused planning",
    text: "You provide details such as experience level, weekly distance, goal race, target time, and training days. Based on proven training principles, the app generates a plan that balances intensity and recovery.",
  },
  {
    title: "Training Philosophy",
    subtitle: "Progress safely, reduce injury risk",
    text: "Plans follow gradual progression, appropriate pacing, and proper recovery. The aim is sustainable performance gains rather than short-term intensity.",
  },
  {
    title: "Important Notice",
    subtitle: "Training guidance, not medical advice",
    text: "This app provides general training recommendations and does not replace professional coaching or medical advice. Always listen to your body.",
  },
  {
    title: "Credits & Support",
    subtitle: "Who made this and how to support",
    text: "Built by Ioannis Psychogyios, runner and Test Automation Engineer. If you enjoy the app, consider supporting development via Buy Me a Coffee or Patreon. Thank you for helping make this project better!",
    supportLinks: [
      {
        label: "Buy Me a Coffee",
        url: "https://buymeacoffee.com/psicaek",
        icon: "mdi-coffee",
        color: "#bef264", // brand yellow/brown
      },
      {
        label: "Patreon",
        url: "https://www.patreon.com/c/psicaek",
        icon: "mdi-patreon",
        color: "#bef264", // Patreon orange-red
      },
      {
        label: "PayPal",
        url: "https://paypal.me/ioannisPsychogyios",
        icon: "mdi-paypal",
        color: "#bef264",
        img: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/PayPal_Logo_Icon_2014.svg/960px-PayPal_Logo_Icon_2014.svg.png",
      },
    ],
  },
];
</script>
