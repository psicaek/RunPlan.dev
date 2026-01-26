<template>
  <v-footer class="d-flex flex-column" color="#bef264">
    <div class="d-flex w-100 align-center px-4 py-2">
      <strong
        style="
          font-family:
            &quot;Gill Sans&quot;, &quot;Gill Sans MT&quot;, Calibri,
            &quot;Trebuchet MS&quot;, sans-serif;
        "
        >Created by Ioannis Psychogyios</strong
      >

      <div class="d-flex ga-2 ms-auto">
        <strong
          style="
            font-family:
              &quot;Gill Sans&quot;, &quot;Gill Sans MT&quot;, Calibri,
              &quot;Trebuchet MS&quot;, sans-serif;
          "
          >Find me and support me:</strong
        >
        <v-btn
          v-for="item in links"
          :key="item.label"
          :href="item.url"
          target="_blank"
          variant="text"
          size="small"
          :aria-label="`Visit ${item.label}`"
        >
          <v-icon v-if="item.icon">{{ item.icon }}</v-icon>

          <img
            v-else
            src="/paypal.svg"
            alt="PayPal"
            style="width: 20px; height: 20px"
          />
        </v-btn>
      </div>
    </div>

    <div class="px-4 py-2 text-center">
      <strong
        d-flex
        ga-2
        ms-auto
        style="
          font-family:
            &quot;Gill Sans&quot;, &quot;Gill Sans MT&quot;, Calibri,
            &quot;Trebuchet MS&quot;, sans-serif;
        "
        >© 2026 Run Plan Generator · v1.0.0</strong
      >
    </div>
  </v-footer>
</template>

<script setup lang="ts">
import { mdiPatreon, mdiInstagram, mdiHeart } from "@mdi/js";

const links = [
  {
    label: "Patreon",
    url: "https://www.patreon.com/c/psicaek",
    icon: mdiPatreon,
    color: "#bef264", // Patreon orange-red
  },
  {
    label: "Instagram",
    icon: mdiInstagram,
    url: "https://www.instagram.com/psic_aek14/",
  },
  {
    label: "PayPal",
    img: "/paypal.svg",
    url: "https://paypal.me/ioannisPsychogyios",
  },
  {
    label: "Donate",
    icon: mdiHeart,
    url: "https://buymeacoffee.com/psicaek",
  },
];
</script>
