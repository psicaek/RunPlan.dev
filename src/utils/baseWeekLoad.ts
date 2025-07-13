export function getWeeklyKm(
  profile: {
    experienceLevel: string;
    weeklyDistance: number;
    gender: string;
    age: number;
  },
  goal: {
    raceDistance: string;
  }
): number {
  const experienceFactor =
    {
      beginner: 0.5,
      intermediate: 0.75,
      advanced: 1,
      expert: 1.25,
      elite: 1.5,
    }[profile.experienceLevel] || 1;

  let minKm = 0;
  let maxKm = 0;
  switch (goal.raceDistance.toLowerCase()) {
    case "5k":
      minKm = 15;
      maxKm = 30;
      break;
    case "10k":
      minKm = 25;
      maxKm = 45;
      break;
    case "half marathon":
    case "hm":
      minKm = 35;
      maxKm = 65;
      break;
    case "marathon":
      minKm = 50;
      maxKm = 90;
      break;
    default:
      minKm = 20;
      maxKm = 40;
  }

  let totalWeeklyKm = experienceFactor * minKm + (maxKm - minKm);

  if (profile.weeklyDistance < totalWeeklyKm) {
    totalWeeklyKm *= 0.8;
  }

  if (profile.gender === "female") {
    totalWeeklyKm *= 0.8;
  }

  if (profile.age > 45 && experienceFactor < 1) {
    totalWeeklyKm *= 0.8;
  }

  return Math.round(totalWeeklyKm);
}
