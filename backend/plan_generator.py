from datetime import datetime


def generate_plan_logic(profile, goal):

    experienceLevel = profile.experienceLevel
    weeklydistance = profile.weeklyDistance
    longestrun = profile.longestRun
    age = profile.age
    race_distance = goal.raceDistance
    goaltime = goal.goalTime
    targetdate = goal.targetDate
    trainingdays = goal.trainingDays  
    personalBest = goal.personalBest



    weeks_until = calculate_weeks_until(targetdate)
    pace = calculate_pace(goaltime, race_distance)
    weekly_type_of_runs = calculate_weekly_type_of_runs(trainingdays)        
    calc_max_volume = calculate_max_volume(experienceLevel,age)   
    weekly_mileage = calculate_weekly_mileage(weeklydistance,race_distance, weeks_until, calc_max_volume,experienceLevel)
    run_per_type = calculate_run_per_type(weekly_mileage,weekly_type_of_runs,trainingdays)
    print(weeks_until)
    print(pace)
    print(weekly_type_of_runs)
    print(calc_max_volume)
    print(weekly_mileage)
    print(run_per_type)

    weeks = []

    for i in range(weeks_until):
        runs = []

        for run_type in weekly_type_of_runs:
            runs.append({
                "type": run_type,
                "distance": round(run_per_type[i][run_type], 1)
                })
        weeks.append({
            "week": i + 1,
            "total_km": round(weekly_mileage[i], 1),
            "runs": runs
        })

    return {
        "weeks_until": weeks_until,
        "pace": pace,
        "weeks": weeks
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
    minutes = int(pace)                  # whole minutes
    seconds = int(round((pace - minutes) * 60))  # remaining seconds

    return f"{minutes}:{seconds:02d}"    # format as MM:SS
    
def calculate_weekly_type_of_runs(training_days):
    days = training_days.lower()
    type_of_runs = []
    if days == "2 days":
        type_of_runs = ["easy", "long"]
        return type_of_runs
    elif days == "3 days":
        type_of_runs = ["easy", "interval", "long"]
        return type_of_runs
    elif days == "4 days":
        type_of_runs = ["easy", "interval", "easy", "long"]
        return type_of_runs
    elif days == "5 days":
        type_of_runs = ["easy", "interval", "easy", "long", "tempo"]
        return type_of_runs
    elif days == "6 days":
        type_of_runs = ["easy", "interval", "easy", "long", "tempo", "recovery"]
        return type_of_runs
    elif days == "7 days":
        type_of_runs = ["easy", "interval", "easy", "long", "tempo", "recovery", "easy"]
        return type_of_runs



def calculate_max_volume(experienceLevel,age):
    
    base_level = 0
    agefactor = age 

    if agefactor > 35:
        base_level +=0.9
    else:
        base_level = 1


    if experienceLevel == "Beginner":
        max_volume = 50 * base_level
    elif experienceLevel == "Intermediate":
        max_volume = 65 * base_level
    elif experienceLevel == "Advanced":
        max_volume = 80 * base_level    
    elif experienceLevel == "Expert":
        max_volume = 100 * base_level
    elif experienceLevel == "Elite":
        max_volume = 150 * base_level

    return max_volume    

def calculate_weekly_mileage(weekly_distance,race_distance, weeks_until, max_volume, experiencelevel):
    mileage_plan = []
    current = weekly_distance
    deload_variable=0
    

    if experiencelevel == "Beginner":
        if race_distance == "5K":
            current = weekly_distance * 0.4
        elif race_distance == "10K":
            current = weekly_distance * 0.6
        elif race_distance == "Half Marathon":
            current = weekly_distance * 0.8
        elif race_distance == "Marathon":
            current = weekly_distance * 1.0    

    elif experiencelevel == "Intermediate":
        if race_distance == "5K":
            current = weekly_distance * 0.6  
        elif race_distance == "10K":
            current = weekly_distance * 0.7 
        elif race_distance == "Half Marathon":
            current = weekly_distance * 0.9
        elif race_distance == "Marathon":
            current = weekly_distance * 1.1                           
       
    elif experiencelevel == "Advanced":
        if race_distance == "5K":
            current = weekly_distance * 0.8
        elif race_distance == "10K":
            current = weekly_distance * 0.9
        elif race_distance == "Half Marathon":
            current = weekly_distance * 1.0     
        elif race_distance == "Marathon":
            current = weekly_distance * 1.2

    elif experiencelevel == "Expert":
        if race_distance == "5K":
            current = weekly_distance * 1.0
        elif race_distance == "10K":
            current = weekly_distance * 1.1
        elif race_distance == "Half Marathon":
            current = weekly_distance * 1.2     
        elif race_distance == "Marathon":
            current = weekly_distance * 1.3        
    elif experiencelevel == "Elite":
        if race_distance == "5K":
            current = weekly_distance * 1.2
        elif race_distance == "10K":
            current = weekly_distance * 1.3
        elif   race_distance == "Half Marathon":
            current = weekly_distance * 1.4         
        elif race_distance == "Marathon":
            current = weekly_distance * 1.5      
                  


    for week in range(weeks_until):
    # Determine number of taper weeks
        taper_weeks = 2 if weeks_until > 12 else max(1, round(weeks_until * 0.1))
       
        progress = week + 1
        
        
        istaper = progress > weeks_until - taper_weeks
        is_normal = progress / weeks_until < 0.7 and not istaper
        is_build = progress/ weeks_until > 0.7 and not istaper
        deload_week = (progress % 4 == 0) and not istaper

        if (is_normal or is_build) and deload_week:
            deload_variable=current
            current *=0.92
            print("deload")
            print(deload_variable)
        elif is_normal:  # first weeks_before_taper
            print(deload_variable)
            if deload_variable> 0:
                current = deload_variable * 1.08
                deload_variable = 0
            else:
               current *= 1.08    
            print("normal")
            
        elif is_build:
            print(deload_variable)
            if deload_variable> 0:
                current = deload_variable * 1.12
                deload_variable = 0
            else:
               current *= 1.12   
            print("build")
            
        elif istaper:
            current*= 0.5 
            print("taper")    
            print(deload_variable)      

        current = round(current, 1)
        current = min(current, max_volume)
        mileage_plan.append(current)

    return mileage_plan      

def calculate_run_per_type(mileage_plan,type_of_runs,trainingdays):
    runs_per_week = []
    for week_mileage in mileage_plan:
        week_runs = {}
        if trainingdays.lower() == "2 days":
            for run_type in type_of_runs:
                if run_type == "easy":
                    week_runs[run_type] = round(week_mileage * 0.4, 1)
                elif run_type == "long":
                    week_runs[run_type] = round(week_mileage * 0.6, 1)
            runs_per_week.append(week_runs)
        elif trainingdays.lower() == "3 days":
            for run_type in type_of_runs:
                if run_type == "easy":
                    week_runs[run_type] = round(week_mileage * 0.25, 1)
                elif run_type == "interval":
                    week_runs[run_type] = round(week_mileage * 0.25, 1)
                elif run_type == "long":
                    week_runs[run_type] = round(week_mileage * 0.5, 1)  
            runs_per_week.append(week_runs)
        elif trainingdays.lower() == "4 days":
            for run_type in type_of_runs:
                if run_type == "easy":
                    week_runs[run_type] = round(week_mileage * 0.2, 1)
                elif run_type == "interval":
                    week_runs[run_type] = round(week_mileage * 0.2, 1)
                elif run_type == "long":
                    week_runs[run_type] = round(week_mileage * 0.4, 1)  
            runs_per_week.append(week_runs)
        elif trainingdays.lower() == "5 days":
            for run_type in type_of_runs:
                if run_type == "easy":
                    week_runs[run_type] = round(week_mileage * 0.15, 1)
                elif run_type == "interval":
                    week_runs[run_type] = round(week_mileage * 0.15, 1)
                elif run_type == "long":
                    week_runs[run_type] = round(week_mileage * 0.4, 1)  
                elif run_type == "tempo":
                    week_runs[run_type] = round(week_mileage * 0.15, 1)   
            runs_per_week.append(week_runs)
        elif trainingdays.lower() == "6 days":
            for run_type in type_of_runs:
                if run_type == "easy":
                    week_runs[run_type] = round(week_mileage * 0.11, 1)
                elif run_type == "interval":
                    week_runs[run_type] = round(week_mileage * 0.11, 1)
                elif run_type == "long":
                    week_runs[run_type] = round(week_mileage * 0.35, 1)  
                elif run_type == "tempo":
                    week_runs[run_type] = round(week_mileage * 0.11, 1)  
                elif run_type == "recovery":
                    week_runs[run_type] = round(week_mileage * 0.1, 1)  
            runs_per_week.append(week_runs)
        elif trainingdays.lower() == "7 days":
            for run_type in type_of_runs:
                if run_type == "easy":
                    week_runs[run_type] = round(week_mileage * 0.15, 1)
                elif run_type == "interval":
                    week_runs[run_type] = round(week_mileage * 0.15, 1)
                elif run_type == "long":
                    week_runs[run_type] = round(week_mileage * 0.3, 1)  
                elif run_type == "tempo":
                    week_runs[run_type] = round(week_mileage * 0.15, 1)  
                elif run_type == "recovery":
                    week_runs[run_type] = round(week_mileage * 0.1, 1)  
            runs_per_week.append(week_runs)                
    return runs_per_week
    
 