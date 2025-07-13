export function getWeeksUntilRace(goal: { targetDate: string }): number {
  const today = new Date();
  const raceDate = new Date(goal.targetDate);

  // Έλεγχος αν η ημερομηνία είναι έγκυρη
  if (isNaN(raceDate.getTime())) {
    throw new Error("Invalid target date");
  }

  // Υπολογισμός διαφοράς σε milliseconds
  const diffInMs = raceDate.getTime() - today.getTime();

  // Μετατροπή σε εβδομάδες
  const weeks = diffInMs / (1000 * 60 * 60 * 24 * 7);

  return Math.max(1, Math.floor(weeks)); // τουλάχιστον 1 εβδομάδα
}
