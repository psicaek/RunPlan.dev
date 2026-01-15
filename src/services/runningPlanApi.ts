// src/services/runningPlanApi.ts

export interface RunningPlanRequest {
  profile: {
    experienceLevel: string;
    weeklyDistance: number;
    longestRun: number;
    age: number;
    gender: string;
  };
  goal: {
    raceDistance: string;
    goalTime: number;
    targetDate: string; // Format: "YYYY-MM-DD"
    trainingDays: string;
    personalBest: number;
  };
}

export interface RunningPlanResponse {
  success: boolean;
  message: string;
  plan?: any;
}

const API_BASE_URL = "http://192.168.178.101:8001";

class RunningPlanApiService {
  /**
   * Send data to backend to generate running plan
   */
  async generatePlan(data: RunningPlanRequest): Promise<RunningPlanResponse> {
    try {
      console.log("Sending to backend:", data);

      const response = await fetch(`${API_BASE_URL}/api/generate-plan`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      console.log("Received from backend:", result);

      return result;
    } catch (error) {
      console.error("API Error:", error);
      throw error;
    }
  }

  /**
   * Check if backend is running
   */
  async healthCheck(): Promise<boolean> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/health`);
      return response.ok;
    } catch (error) {
      console.error("Backend is not running:", error);
      return false;
    }
  }
}

export const runningPlanApi = new RunningPlanApiService();
