<template>
  <v-app>
   <v-main class="gradient-bg">
       <v-container style="max-width: 1900px">
  <v-row align="center" justify="center" class="mb-4">
    <!-- Logo -->
    <v-col cols="auto">
      <v-img
        src ="src/assets/mainLogo.svg"
        alt="Run Plan Logo"
        width="60"
        class="mb-1"
      ></v-img>
    </v-col>
    <v-col>
      <!-- Title & Subtitle -->
    <h1 class="text-h5 font-weight-bold mb-0">Run Plan Generator</h1>
    
    <p class="text-subtitle-2">Create your personalized running plan in minutes!</p>
    </v-col>
</v-row>
</v-container>
 </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'AthletsProfile',
};

</script>



<style scoped>
.gradient-bg {
  background: linear-gradient(to bottom, #00b4db, #001f3f);
  min-height: 100vh;
}
</style>