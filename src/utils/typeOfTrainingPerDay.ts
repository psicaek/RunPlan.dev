interface WorkoutDay {
  trainingDays: string;
  type: string;
}

export function assignTrainingTypes(
  trainingDays: string,
  phase: "endurance" | "speed" | "taper"
): WorkoutDay[] {
  const numDays = trainingDays.length;
  const days: WorkoutDay[] = [];

  for (let i = 0; i < numDays; i++) {
    let type = "easy run";

    if (phase === "endurance") {
      if (i === numDays - 1) {
        type = "long run";
      }
    } else if (phase === "speed") {
      if (i === numDays - 2) {
        type = "intervals";
      } else if (i === numDays - 1) {
        type = "long run";
      }
    } else if (phase === "taper") {
      if (i === numDays - 1) {
        type = "short long run";
      }
    }

    days.push({
      trainingDays: trainingDays[i],
      type,
    });
  }

  return days;
}
