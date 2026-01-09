<template>
  <v-app>
    
    <v-navigation-drawer
      v-model="drawer"
      :rail="rail"
      permanent
      @click.stop = "rail = !rail"
      style="
        background: linear-gradient(
          135deg,
          #00b4db,
          0%,
          #001f3f 100%
        ) !important;
      "
      color: aliceblue
    >
      <v-list>
        <v-list-item prepend-avatar="src/assets/mainLogo.svg" title="Run Plan" style="color: aliceblue">
          <template v-slot:append>
            <v-btn
              icon="mdi-chevron-left"
              variant="text"
              style="color: aliceblue"
              :rail="rail"
              @click.stop = "rail = !rail"
            ></v-btn>
          </template>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item
          prepend-icon="mdi-home-city"
          title="Home"
          to="/"
          style="color: aliceblue"
        />

        <v-list-item
          prepend-icon="mdi-account"
          title="About"
          to="/about"
          style="color: aliceblue"
        />

        <v-list-item
          prepend-icon="mdi-run-fast"
          
          title="Run Plan "
          to="/"
          style="color: aliceblue"
        />
      </v-list>
    </v-navigation-drawer>

    <router-view></router-view>
  </v-app>
</template>

<script>
import { ref } from 'vue'

import router from './router';

function home() {
  router.push({ name: "Home"})
}

export default {
  name: "App",
  setup() {
    const drawer = ref(true)
    const rail = ref(true)

    return {
      drawer,
      rail,
    }
  },
}
</script>

