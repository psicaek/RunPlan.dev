<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <header class="p-4 bg-white shadow">
      <nav class="flex justify-between">
        <router-link to="/">🏃 RunPlan.dev</router-link>
        <div>
          <router-link to="/generate" class="mr-4">Generator</router-link>
          <router-link to="/about">About</router-link>
        </div>
      </nav>
    </header>
    <main class="p-4">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>
