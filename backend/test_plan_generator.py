import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
from plan_generator import (
    calculate_weeks_until,
    calculate_pace,
    format_pace,
    calculate_weekly_type_of_runs,
    calculate_weekly_mileage,
    calculate_max_volume,
    calculate_run_pace,
    calculate_run_per_type
    
)



class TestCalculateWeeksUntil:
    @patch("plan_generator.datetime")
    def test_exact_weeks(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime

        assert calculate_weeks_until("2026-02-03") == 4

    @patch("plan_generator.datetime")
    def test_partial_weeks_floor(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime

        assert calculate_weeks_until("2026-01-20") == 2

    @patch("plan_generator.datetime")
    def test_past_date(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime

        assert calculate_weeks_until("2025-12-01") == 0

    @patch("plan_generator.datetime")
    def test_same_day(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime

        assert calculate_weeks_until("2026-01-06") == 0


# --------------------------------------------------
# calculate_pace + format_pace
# --------------------------------------------------

class TestCalculatePace:

    def test_5k_pace_seconds(self):
        pace = calculate_pace(25, "5K")
        assert pace == 300  # seconds per km
        assert format_pace(pace) == "5:00"

    def test_10k_pace(self):
        pace = calculate_pace(50, "10K")
        assert pace == 300

    def test_half_marathon_pace(self):
        pace = calculate_pace(105.4875, "Half Marathon")
        assert pytest.approx(pace, abs=1) == 300

    def test_marathon_pace(self):
        pace = calculate_pace(210.975, "Marathon")
        assert pytest.approx(pace, abs=1) == 300

    def test_zero_time(self):
        pace = calculate_pace(0, "5K")
        assert pace == 0


# --------------------------------------------------
# calculate_weekly_type_of_runs
# --------------------------------------------------

class TestCalculateWeeklyTypeOfRuns:
    
    def test_2_days(self):
        assert calculate_weekly_type_of_runs("2 days") == ["easy", "long"]

    def test_3_days(self):
        assert calculate_weekly_type_of_runs("3 days") == ["easy", "interval", "long"]

    def test_4_days(self):
        assert calculate_weekly_type_of_runs("4 days") == [
            "easy", "interval", "long", "recovery"
        ]

    def test_5_days(self):
        assert calculate_weekly_type_of_runs("5 days") == [
            "easy", "interval", "tempo", "long", "recovery"
        ]

    def test_6_days(self):
        assert calculate_weekly_type_of_runs("6 days") == [
            "easy", "interval", "easy", "tempo", "long", "recovery"
        ]

    def test_7_days(self):
        assert calculate_weekly_type_of_runs("7 days") == [
            "easy", "interval", "easy", "long", "tempo", "recovery", "easy"
        ]

    def test_case_insensitive(self):
        assert calculate_weekly_type_of_runs("3 DAYS") == [
            "easy", "interval", "long"
        ]

    def test_invalid_input(self):
        assert calculate_weekly_type_of_runs("8 days") is None

    def test_1_day(self):
        assert calculate_weekly_type_of_runs("1 days") is None    

    def test_0_day(self):
        assert calculate_weekly_type_of_runs("0 days") is None  

# --------------------------------------------------
# calculate_weekly_mileage
# --------------------------------------------------

class TestCalculateWeeklyMileage:

    def test_beginner_5k(self):
        max_volume = calculate_max_volume("Beginner", 30)
        result = calculate_weekly_mileage(
            weekly_distance=20,
            race_distance="5K",
            weeks_until=8,
            max_volume=max_volume,
            experiencelevel="Beginner"
        )

        assert len(result) == 8
        assert result[0] > 0
        assert result[-1] < result[-2]  # taper

    def test_intermediate_marathon_progression(self):
        max_volume = calculate_max_volume("Intermediate", 35)
        result = calculate_weekly_mileage(
            40, "Marathon", 12, max_volume, "Intermediate"
        )

        assert len(result) == 12
        assert max(result) <= max_volume

    def test_elite_volume_cap(self):
        max_volume = calculate_max_volume("Elite", 28)
        result = calculate_weekly_mileage(
            90, "Marathon", 16, max_volume, "Elite"
        )

        assert max(result) <= max_volume

    def test_zero_weeks(self):
        max_volume = calculate_max_volume("Beginner", 40)
        result = calculate_weekly_mileage(
            30, "10K", 0, max_volume, "Beginner"
        )

        assert result == []


class TestCalculateRunPace:

    def test_easy_slower_than_race_pace(self):
        base = 300
        result = calculate_run_pace(base, "easy", "intermediate", 30)
        assert result > base

    def test_interval_faster_than_race_pace(self):
        base = 300
        result = calculate_run_pace(base, "interval", "advanced", 28)
        assert result < base

    def test_teen_runner_faster(self):
        base = 300
        result = calculate_run_pace(base, "tempo", "intermediate", 16)
        assert result < base

    def test_older_runner_slower(self):
        base = 300
        result = calculate_run_pace(base, "easy", "intermediate", 55)
        assert result > base

    def test_unknown_run_type_defaults_to_base(self):
        base = 300
        result = calculate_run_pace(base, "unknown", "advanced", 30)
        assert result != 0

    @pytest.mark.parametrize("experience", [
        "beginner", "intermediate", "advanced", "expert", "elite"
    ])
    def test_all_experience_levels(self, experience):
        result = calculate_run_pace(300, "easy", experience, 30)
        assert isinstance(result, int)


class TestCalculateMaxVolume:

    def test_beginner_under_35(self):
        assert calculate_max_volume("Beginner", 30) == 50

    def test_beginner_over_35_reduction(self):
        assert calculate_max_volume("Beginner", 50) == 45

    def test_elite_volume(self):
        assert calculate_max_volume("Elite", 28) == 150

    def test_elite_over_35(self):
        assert calculate_max_volume("Elite", 45) == 135


class TestCalculateRunPerType:

    def test_3_day_distribution(self):
        mileage = [30]
        types = ["easy", "interval", "long"]
        result = calculate_run_per_type(mileage, types, "3 days")

        week = result[0]
        assert pytest.approx(sum(week.values()), abs=0) == 30

    def test_5_day_distribution_sum(self):
        mileage = [50]
        types = ["easy", "interval", "tempo", "long", "recovery"]
        result = calculate_run_per_type(mileage, types, "5 days")

        week = result[0]
        assert pytest.approx(sum(week.values()), abs=0) == 50

    def test_multiple_weeks(self):
        mileage = [30, 32, 28]
        types = ["easy", "interval", "long"]
        result = calculate_run_per_type(mileage, types, "3 days")

        assert len(result) == 3

    def test_4_day_distribution_sum(self):
        mileage = [50]
        types = ["easy", "interval", "long", "recovery"]
        result = calculate_run_per_type(mileage, types, "4 days")

        week = result[0]
        assert pytest.approx(sum(week.values()), abs=0) == 50   

    def test_6_day_distribution_sum(self):
        mileage = [50]  
        weekly_type_of_runs = calculate_weekly_type_of_runs("6 days")
        result = calculate_run_per_type(mileage, weekly_type_of_runs, "6 days")
        
        week = result[0]
        total = sum(distance * weekly_type_of_runs.count(run_type)
        for run_type, distance in week.items())

        assert pytest.approx(total, abs=0.1) == 50

    def test_7_day_distribution_sum(self):
        mileage = [50]  
        weekly_type_of_runs = calculate_weekly_type_of_runs("7 days")
        result = calculate_run_per_type(mileage, weekly_type_of_runs, "7 days")
        
        week = result[0]
        total = sum(distance * weekly_type_of_runs.count(run_type)
        for run_type, distance in week.items())

        assert pytest.approx(total, abs=0.1) == 50   
# --------------------------------------------------
# Integration sanity test
# --------------------------------------------------

class TestIntegration:

    @patch("plan_generator.datetime")
    def test_end_to_end_flow(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime

        weeks = calculate_weeks_until("2026-04-30")
        pace = calculate_pace(180, "Half Marathon")
        run_types = calculate_weekly_type_of_runs("5 days")

        max_volume = calculate_max_volume("Beginner", 30)
        mileage = calculate_weekly_mileage(
            20, "10K", weeks, max_volume, "Beginner"
        )

        assert weeks > 10
        assert isinstance(pace, int)
        assert ":" in format_pace(pace)
        assert "long" in run_types
        assert len(mileage) == weeks
        assert mileage[-1] < mileage[-2]