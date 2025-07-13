import { getWeeksUntilRace } from "./totalWeeksuntilRace";

interface WorkoutDay {
  day: string;
  type: string;
  distance: number;
}

interface Pace {
  targetTime: number;
}

interface WeeklyPlan {
  week: number;
  phase: "endurance" | "speed" | "taper";
  weekKm: number;
  days: WorkoutDay[];
}

interface GoalInput {
  targetDate: string;
  trainingDays: string; // π.χ. "Mon,Wed,Fri"
}

export function generateFullTrainingPlan(
  goal: GoalInput,
  baseKm: number
): WeeklyPlan[] {
  const totalWeeks = getWeeksUntilRace(goal);
  const taperWeeks = 2;
  const speedWeeks = Math.min(6, Math.floor(totalWeeks * 0.3));
  const enduranceWeeks = totalWeeks - taperWeeks - speedWeeks;

  const trainingDaysArray = goal.trainingDays
    .split(",")
    .map((d) => d.trim())
    .filter((d) => d); // clean empty entries

  const plan: WeeklyPlan[] = [];

  for (let week = 1; week <= totalWeeks; week++) {
    let phase: "endurance" | "speed" | "taper" = "endurance";
    if (week > enduranceWeeks && week <= enduranceWeeks + speedWeeks) {
      phase = "speed";
    } else if (week > enduranceWeeks + speedWeeks) {
      phase = "taper";
    }

    // Week KM with 7% progressive increase
    let weekKm = baseKm * Math.pow(1.07, week - 1);
    if (week % 4 === 0) weekKm *= 0.85; // recovery week
    if (phase === "taper") weekKm *= 0.6;
    const numDays = trainingDaysArray.length;
    let longRunKm = phase === "taper" ? weekKm * 0.3 : weekKm * 0.35;
    let intervalsKm =
      phase === "speed" || phase === "endurance" ? weekKm * 0.2 : 0;
    let remainingKm = weekKm - longRunKm - intervalsKm;
    let easyDays = phase === "speed" ? numDays - 3 : numDays - 1; // αφαιρούμε intervals και long run
    let easyKmPerDay = easyDays > 0 ? remainingKm / easyDays : 0;
    let intervalsPerDay = intervalsKm / 2;

    // Assign training type per day
    const days: WorkoutDay[] = trainingDaysArray.map((day, i) => {
      let type = "easy run";
      let distance = easyKmPerDay;

      if (phase === "endurance" && i === trainingDaysArray.length - 1) {
        type = "long run";
        distance = longRunKm;
      } else if (phase === "endurance" && i === trainingDaysArray.length - 2) {
        type = "intervals";
        distance = intervalsPerDay;
      } else if (phase === "speed") {
        if (i === trainingDaysArray.length - 3) {
          type = "intervals";
          distance = intervalsPerDay;
        } else if (i === trainingDaysArray.length - 2) {
          type = "intervals";
          distance = intervalsPerDay;
        } else if (i === trainingDaysArray.length - 1) {
          type = "long run";
          distance = longRunKm;
        }
      } else if (phase === "taper" && i === trainingDaysArray.length - 1) {
        type = "short long run";
        distance = longRunKm;
      }
      if (
        phase === "taper" &&
        i === trainingDaysArray.length - 1 &&
        week === totalWeeks
      )
        type = "Race Day";
      return { day, type, distance: Math.round(distance) };
    });

    plan.push({
      week,
      phase,
      weekKm: Math.round(weekKm),
      days,
    });
  }

  return plan;
}
