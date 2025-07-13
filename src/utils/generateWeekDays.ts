export function getweekDates(goal: { trainingDays: string }): string[] {
  // 1. Μετατρέπουμε το string που παίρνουμε (πχ "4") σε αριθμό
  const daysCount = parseInt(goal.trainingDays, 10);

  // 2. Αν το αποτέλεσμα δεν είναι αριθμός ή είναι μικρότερο ή ίσο του 0, επιστρέφουμε κενό array
  if (isNaN(daysCount) || daysCount <= 0) return [];

  // 3. Ορίζουμε τη λίστα των προτιμητέων ημερών της εβδομάδας (αρχίζοντας από Δευτέρα)
  const preferredDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

  // 4. Δημιουργούμε έναν χάρτη (object) που αντιστοιχεί αριθμό ημερών σε συγκεκριμένη λίστα με ημέρες.
  //    Πχ αν θέλει 3 μέρες, του δίνουμε ["Mon", "Wed", "Fri"]
  const predefinedDaysMap: { [key: number]: string[] } = {
    1: ["Wed"],
    2: ["Tue", "Thu"],
    3: ["Mon", "Wed", "Fri"],
    4: ["Mon", "Wed", "Fri", "Sun"],
    5: ["Mon", "Tue", "Wed", "Fri", "Sun"],
    6: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sun"],
    7: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
  };

  // 5. Ελέγχουμε αν έχουμε προκαθορισμένες ημέρες για τον αριθμό που δόθηκε.
  //    Αν ναι, τις επιστρέφουμε.
  if (predefinedDaysMap[daysCount]) {
    return predefinedDaysMap[daysCount];
  }

  // 6. Αν δεν έχουμε προκαθορισμένες ημέρες, παίρνουμε τις πρώτες n ημέρες από την
  //    προτιμητέα λίστα (πχ αν θέλει 3, παίρνουμε ["Mon", "Tue", "Wed"])
  return preferredDays.slice(0, daysCount);
}
