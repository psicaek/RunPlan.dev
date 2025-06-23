<template>
  <v-container class="pa-4" fluid>
    <v-row>
      <v-col cols="12" md="6" offset-md="3">
        <v-card>
          <v-card-title class="text-h5">Running Plan Generator</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="generatePlan" ref="form">
              <v-text-field
                v-model="days"
                label="Ημέρες ανά εβδομάδα"
                type="number"
                :rules="[value => (value >= 1 && value <= 7) || '1-7 days']"
                required
              ></v-text-field>

              <v-text-field
                v-model="goal"
                label="Στόχος (χλμ/εβδομάδα)"
                type="number"
                :rules="[value => value > 0 || 'Positive number required']"
                required
              ></v-text-field>

              <v-btn color="primary" type="submit">Δημιουργία Πλάνου</v-btn>
            </v-form>
          </v-card-text>
        </v-card>

        <v-card v-if="plan.length" class="mt-4">
          <v-card-title>Πλάνο Προπόνησης</v-card-title>
          <v-list>
            <v-list-item v-for="(item, index) in plan" :key="index">
              <v-list-item-content>
                <v-list-item-title>Ημέρα {{ index + 1 }}: {{ item }} χλμ</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      days: 3,
      goal: 15,
      plan: [],
    };
  },
  methods: {
    generatePlan() {
      const base = Math.floor(this.goal / this.days);
      const remainder = this.goal % this.days;
      this.plan = Array(this.days).fill(base);

      for (let i = 0; i < remainder; i++) {
        this.plan[i]++;
      }
    },
  },
};
</script>
