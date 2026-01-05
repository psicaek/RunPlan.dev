import { defineStore } from "pinia";
import {
  runningPlanApi,
  type RunningPlanRequest,
} from "../services/runningPlanApi";
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
    trainingPlan: [] as Array<{
      week: number;
      phase: string;
      weekKm: number;
      days?: Array<{
        day: string;
        type: string;
        distance: number;
        pace?: string;
      }>;
    }>,
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
    /**
     * Reset all data
     */
    resetStore() {
      this.profile = {
        experienceLevel: "",
        weeklyDistance: 0,
        longestRun: 0,
        age: 0,
        gender: "",
      };
      this.goal = {
        raceDistance: "",
        goalTime: 0,
        targetDate: null,
        trainingDays: "",
      };
      this.trainingPlan = null;
      this.isGenerating = false;
      this.generationError = null;
    },

    /**
     * Generate Training Plan - API Call
     */
    async generateTrainingPlan() {
      // Validate data
      if (!this.isProfileComplete() || !this.isGoalComplete()) {
        this.generationError = "Please complete all fields first";
        return;
      }

      this.isGenerating = true;
      this.generationError = null;

      try {
        // Check if backend is running
        const isHealthy = await runningPlanApi.healthCheck();
        if (!isHealthy) {
          throw new Error(
            "Backend is not running. Please start the Python server at http://localhost:8000"
          );
        }

        // Convert Date to string format (YYYY-MM-DD)
        const targetDateStr = this.goal.targetDate
          ? this.goal.targetDate.toISOString().split("T")[0]
          : "";

        // Prepare data for API
        const requestData: RunningPlanRequest = {
          profile: {
            experienceLevel: this.profile.experienceLevel,
            weeklyDistance: this.profile.weeklyDistance || 0,
            longestRun: this.profile.longestRun || 0,
            age: this.profile.age || 0,
            gender: this.profile.gender,
          },
          goal: {
            raceDistance: this.goal.raceDistance,
            goalTime: this.goal.goalTime || 0,
            targetDate: targetDateStr,
            trainingDays: this.goal.trainingDays,
          },
        };

        console.log("Sending to backend:", requestData);

        // Call API
        const response = await runningPlanApi.generatePlan(requestData);

        console.log("Received from backend:", response);

        // Store the result
        this.trainingPlan = response.data;

        return response;
      } catch (error) {
        console.error("Error generating plan:", error);
        this.generationError =
          error instanceof Error ? error.message : "Unknown error";
        throw error;
      } finally {
        this.isGenerating = false;
      }
    },
  },
});
