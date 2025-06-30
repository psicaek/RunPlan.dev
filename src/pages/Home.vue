<template>
  <v-app>
    <v-main class="gradient-bg">
      <v-container style="max-width: 1900px">
        <v-row align="center" justify="center" class="mb-4">
          <!-- Logo -->
          <v-col cols="auto">
            <v-img
              src="src/assets/mainLogo.svg"
              alt="Run Plan Logo"
              width="60"
              class="mb-1"
            ></v-img>
          </v-col>
          <v-col>
            <!-- Title & Subtitle -->
            <h1 class="text-h5 font-weight-bold mb-0">Run Plan Generator</h1>

            <p class="text-subtitle-2">
              Create your personalized running plan in minutes!
            </p>
          </v-col>
        </v-row>
      </v-container>
      <!-- Title & Subtitle -->
      <v-col> </v-col>

      <v-container class="text-center white--text">
        <v-row>
          <v-col cols="12" sm="6" offset-sm="3">
            <p class="page-title-text">
              Create your personalized running plan in minutes!
            </p>
            <p class="page-second-text">
              Answer a few questions and get a tailored plan to help you achieve
              your running goals.
            </p>
          </v-col>
        </v-row>
      </v-container>
      <v-row class="text-center">
        <v-col cols="12" sm="6" offset-sm="3">
          <v-btn
            color="primary"
            class="mt-5"
            @click="$router.push('/athletsProfile')"
          >
            Get Started
          </v-btn>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
.gradient-bg {
  background: linear-gradient(to bottom, #00b4db, #001f3f);
  min-height: 100vh;
}
.page-title-text {
  font-size: 25px;
  font-family: Helvetica-Neue;
  color: #000000;
}
.page-second-text {
  font-size: 18px;
  font-family: Helvetica-Neue;
  color: #000000;
}
</style>
