// main.js
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";
import { createHead } from '@vueuse/head'

import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

// 👇 ICONS
import { aliases, mdi } from "vuetify/iconsets/mdi-svg";

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: "mdi",
    aliases,
    sets: {
      mdi,
    },
  },
});
const head = createHead()
const app = createApp(App);
const pinia = createPinia();
app.use(pinia);
app.use(head);
app.use(router);
app.use(vuetify);
app.mount("#app");
