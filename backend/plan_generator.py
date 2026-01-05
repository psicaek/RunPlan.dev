from datetime import datetime


    

def generate_plan_logic(profile, goal):

    experiencelevel = profile.experienceLevel
    weeklydistance = profile.weeklyDistance
    longestrun = profile.longestRun
    age = profile.age
    race_distance = goal.raceDistance
    goaltime = goal.goalTime
    targetdate = goal.targetDate
    trainingdays = goal.trainingDays  

    weeks_until = calculate_weeks_until(targetdate)
    pace = calculate_pace(goaltime, race_distance)
    weekly_type_of_runs = calculate_weekly_type_of_runs(trainingdays)           
    weekly_mileage = calculate_weekly_mileage(weeklydistance, weeks_until)
    print(weeks_until)
    print(pace)
    print(weekly_type_of_runs)
    print(weekly_mileage)

    return {
        "weeks_until": weeks_until,
        "pace": float (pace),
        "weekly_type_of_runs": weekly_type_of_runs,
        "weekly_mileage": weekly_mileage
    }
    
   

def calculate_weeks_until(targetdate):
    today = datetime.now()
    target = datetime.strptime(targetdate, "%Y-%m-%d")
    delta = target - today
    return max(delta.days // 7, 0)
    
def calculate_pace(goal_time, race_distance):
    
    if race_distance == "5K":
        pace = goal_time / 5
    elif race_distance == "10K":
        pace = goal_time / 10
    elif race_distance == "Half Marathon":
        pace = goal_time / 21.0975
    elif race_distance == "Marathon":
        pace = goal_time / 42.195
    return pace # minutes per km
    
def calculate_weekly_type_of_runs(training_days):
    days = training_days.lower()
    if days == "2 days":
        return ["easy", "long"] 
    elif days == "3 days":
        return ["easy", "long", "tempo"]
    elif days == "4 days":
        return ["easy", "interval", "long", "tempo"]
    elif days == "5 days":
        return ["easy", "interval", "easy", "long", "tempo"]
    elif days == "6 days":
        return ["easy", "interval", "easy", "long", "tempo", "recovery"]
    elif days == "7 days":
        return ["easy", "interval", "easy", "long", "tempo", "recovery", "easy"]      


def calculate_weekly_mileage(weekly_distance, weeks_until):
    mileage_plan = []
    current = weekly_distance

    for week in range(weeks_until):
        if week < weeks_until * 0.7:
            current *= 1.08   # max 8% increase
        if week >= weeks_until * 0.8:
            current *= 1.12    # max 12% increase
        if week >= weeks_until * 0.9:   
            current *= 0.8    # tapering
        current = round(current) 
        mileage_plan.append(round(current, 1))

    return mileage_plan      