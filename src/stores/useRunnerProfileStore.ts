import { defineStore } from "pinia";

export const useRunnerProfileStore = defineStore("runnerProfile", {
  state: () => ({
    // 🏃‍♂️ Athlete Profile
    profile: {
      experienceLevel: "" as string,
      weeklyDistance: (0 as number) || null,
      longestRun: (0 as number) || null,
      age: (0 as number) || null,
      gender: "" as string,
    },

    // 🎯 Training Goal
    goal: {
      raceDistance: "" as string,
      goalTime: (0 as number) || null, // σε λεπτά
      targetDate: null as Date | null,
      trainingDays: "" as string,
    },

    // 🗓️ Generated Plan (προαιρετικά για επόμενο βήμα)
    plan: null as string | null,
  }),
  actions: {
    isProfileComplete() {
      const p = this.profile;
      return (
        p.experienceLevel.trim() !== "" &&
        p.gender.trim() !== "" &&
        p.weeklyDistance > 0 &&
        p.longestRun > 0 &&
        p.age > 0
      );
    },

    isGoalComplete() {
      const g = this.goal;
      console.log({
        raceDistance: g.raceDistance,
        goalTime: g.goalTime,
        trainingDays: g.trainingDays,
        targetDate: g.targetDate,
      });
      return (
        g.raceDistance.trim() !== "" &&
        g.goalTime > 0 &&
        g.trainingDays.trim() !== "" &&
        g.targetDate instanceof Date &&
        !isNaN(g.targetDate.getTime())
      );
    },
  },
});
