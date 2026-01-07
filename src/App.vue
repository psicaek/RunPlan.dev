<template>
  <v-app>
    <v-layout>
      <!-- Blue gradient app bar matching your form page -->
      <v-app-bar
        color="primary"
        dark
        elevation="0"
        style="
          background: linear-gradient(
            135deg,
            #00b4db,
            0%,
            #001f3f 100%
          ) !important;
        "
      >
        <v-app-bar-nav-icon
          ><v-img
            src="src/assets/mainLogo.svg"
            width="30"
            height="30"
            class="mr-2"
          ></v-img
        ></v-app-bar-nav-icon>

        <div class="d-flex align-center">
          <span class="font-weight-bold text-h6">RunPlan.dev</span>
        </div>

        <v-spacer></v-spacer>

        <v-btn to="/generate" text class="mr-4"> Generator </v-btn>
        <v-btn to="/about" text> About </v-btn>
      </v-app-bar>

      <v-main>
        <router-view></router-view>
      </v-main>
    </v-layout>
  </v-app>
</template>

<script>
export default {
  name: "App",
};
</script>
