<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :rail="rail"
      permanent
      @click.stop="rail = !rail"
      style="
        background: linear-gradient(
          135deg,
          rgba(190, 242, 100.1),
          40%,
          rgba(190, 242, 100.1) 100%
        ) !important;
      "
    >
      <v-list>
        <v-list-item prepend-avatar="src/assets/mainLogoRevert.svg">
          <template #title>
            <span style="font-size: larger; font-weight: bold; color: #1e293b"
              >Run Plan</span
            >
          </template>
          <template v-slot:append style="font-size: large">
            <v-btn
              icon="mdi-chevron-left"
              variant="text"
              style="color: #1e293b; font-size: xx-large"
              :rail="rail"
              @click.stop="rail = !rail"
            ></v-btn>
          </template>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item to="/" style="color: #1e293b">
          <template #prepend>
            <v-icon size="32">mdi-home-city</v-icon>
          </template>
          <template #title>
            <span style="font-size: larger; font-weight: bold; color: #1e293b"
              >Home</span
            >
          </template>
        </v-list-item>

        <v-list-item to="/about" style="color: #1e293b">
          <template #prepend>
            <v-icon size="35">mdi-account</v-icon>
          </template>
          <template #title>
            <span style="font-size: larger; font-weight: bold; color: #1e293b"
              >About</span
            >
          </template>
        </v-list-item>

        <v-list-item to="/" style="color: #1e293b">
          <template #prepend>
            <v-icon size="32">mdi-run-fast</v-icon>
          </template>
          <template #title>
            <span style="font-size: larger; font-weight: bold; color: #1e293b"
              >Run Plan</span
            >
          </template>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main class="gradient-bg">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import { ref } from "vue";

import router from "./router";

function home() {
  router.push({ name: "Home" });
}

export default {
  name: "App",
  setup() {
    const drawer = ref(true);
    const rail = ref(true);

    return {
      drawer,
      rail,
    };
  },
};
</script>
