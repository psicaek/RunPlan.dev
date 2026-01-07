import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
from plan_generator import calculate_weeks_until, calculate_pace, calculate_weekly_type_of_runs, calculate_weekly_mileage



class TestCalculateWeeksUntil:
    """Test suite for calculate_weeks_until function"""
    
    @patch('plan_generator.datetime')
    def test_future_date_exact_weeks(self, mock_datetime):
        """Test calculation with a future date that's exactly N weeks away"""
        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime
        
        result = calculate_weeks_until("2026-02-03")  # 4 weeks later
        print(result)
        assert result == 4
    
    @patch('plan_generator.datetime')
    def test_future_date_partial_week(self, mock_datetime):
        """Test that partial weeks are rounded down"""
        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime
        
        result = calculate_weeks_until("2026-01-20")  # 14 days = 2 weeks
        print(result)
        assert result == 2
    
    @patch('plan_generator.datetime')
    def test_past_date_returns_zero(self, mock_datetime):
        """Test that past dates return 0, not negative values"""
        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime
        
        result = calculate_weeks_until("2025-12-01")
        print(result)
        assert result == 0
    
    @patch('plan_generator.datetime')
    def test_same_day_returns_zero(self, mock_datetime):
        """Test that today's date returns 0"""
        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime
        
        result = calculate_weeks_until("2026-01-06")
        print(result)
        assert result == 0


class TestCalculatePace:
    """Test suite for calculate_pace function"""
    
    def test_5k_pace_calculation(self):
        """Test pace calculation for 5K race"""
        result = calculate_pace(25, "5K")  # 25 minutes for 5K
        assert result == "5:00"  # 5 min/km
    
    def test_10k_pace_calculation(self):
        """Test pace calculation for 10K race"""
        result = calculate_pace(50, "10K")  # 50 minutes for 10K
        assert result == "5:00"  # 5 min/km
    
    def test_half_marathon_pace_calculation(self):
        """Test pace calculation for Half Marathon"""
        result = calculate_pace(105.4875, "Half Marathon")
        assert pytest.approx(result, 0.01) == "5:00"  # ~5 min/km
    
    def test_marathon_pace_calculation(self):
        """Test pace calculation for Marathon"""
        result = calculate_pace(210.975, "Marathon")
        assert pytest.approx(result, 0.01) == "5:00"  # ~5 min/km
    
    def test_zero_time(self):
        """Test edge case with zero goal time"""
        result = calculate_pace(0, "5K")
        assert result == "0:00"
    
    def test_invalid_race_distance(self):
        """Test that invalid race distance returns None or raises error"""
        with pytest.raises(UnboundLocalError):
            calculate_pace(30, "invalid_distance")


class TestCalculateWeeklyTypeOfRuns:
    """Test suite for calculate_weekly_type_of_runs function"""
    
    def test_2_days_training(self):
        """Test run types for 2 days training"""
        result = calculate_weekly_type_of_runs("2 days")
        assert result == ["easy", "long"]
    
    def test_3_days_training(self):
        """Test run types for 3 days training"""
        result = calculate_weekly_type_of_runs("3 days")
        assert result == ["easy", "interval", "long"]
    
    def test_4_days_training(self):
        """Test run types for 4 days training"""
        result = calculate_weekly_type_of_runs("4 days")
        assert result == ["easy", "interval", "easy", "long"]
    
    def test_5_days_training(self):
        """Test run types for 5 days training"""
        result = calculate_weekly_type_of_runs("5 days")
        assert result == ["easy", "interval", "easy", "long", "tempo"]
    
    def test_6_days_training(self):
        """Test run types for 6 days training"""
        result = calculate_weekly_type_of_runs("6 days")
        assert result == ["easy", "interval", "easy", "long", "tempo", "recovery"]
    
    def test_7_days_training(self):
        """Test run types for 7 days training"""
        result = calculate_weekly_type_of_runs("7 days")
        assert result == ["easy", "interval", "easy", "long", "tempo", "recovery", "easy"]
    
    def test_case_insensitive(self):
        """Test that input is case insensitive"""
        result = calculate_weekly_type_of_runs("3 DAYS")
        assert result == ["easy", "interval", "long"]
    
    def test_invalid_days_returns_none(self):
        """Test that invalid input returns None"""
        result = calculate_weekly_type_of_runs("8 days")
        assert result is None


class TestCalculateWeeklyMileage:
    """Test suite for calculate_weekly_mileage function"""
    
    def test_beginner_5k_mileage_plan(self):
        """Test mileage plan for beginner 5K"""
        result = calculate_weekly_mileage(20, "5K", 8, "Beginner")
        assert len(result) == 8
        assert result[0] > 0  # First week should be positive
        assert result[-1] < result[-2]  # Taper in final week
    
    def test_intermediate_marathon_progression(self):
        """Test that intermediate marathon plan increases progressively"""
        result = calculate_weekly_mileage(40, "Marathon", 12, "Intermediate")
        assert len(result) == 12
        # Check progression in build phase (first 70% of weeks)
        build_weeks = int(12 * 0.7)
        for i in range(build_weeks - 1):
            assert result[i + 1] > result[i], f"Week {i+1} should be more than week {i}"
    
    def test_advanced_half_marathon(self):
        """Test advanced half marathon plan"""
        result = calculate_weekly_mileage(50, "Half Marathon", 10, "Advanced")
        assert len(result) == 10
        assert all(week > 0 for week in result)
    
    def test_expert_10k(self):
        """Test expert 10K plan"""
        result = calculate_weekly_mileage(60, "10K", 6, "Expert")
        assert len(result) == 6
    
    def test_elite_marathon(self):
        """Test elite marathon plan with highest multiplier"""
        result = calculate_weekly_mileage(80, "Marathon", 16, "Elite")
        assert len(result) == 16
        # Elite should start with highest base (1.5x)
        assert result[0] > 100
    
    def test_taper_phase(self):
        """Test that taper phase reduces mileage"""
        result = calculate_weekly_mileage(40, "Marathon", 10, "Intermediate")
        # Last week (taper) should be less than second-to-last
        assert result[-1] < result[-2]
    
    def test_single_week_plan(self):
        """Test edge case with only 1 week"""
        result = calculate_weekly_mileage(30, "Half Marathon", 1, "Beginner")
        assert len(result) == 1
        assert result[0] > 0
    
    def test_zero_weeks(self):
        """Test edge case with 0 weeks"""
        result = calculate_weekly_mileage(30, "Half Marathon", 0, "Beginner")
        assert len(result) == 0
    
    @pytest.mark.parametrize("experience_level", [
        "Beginner", "Intermediate", "Advanced", "Expert", "Elite"
    ])
    def test_all_experience_levels(self, experience_level):
        """Test that all experience levels produce valid plans"""
        result = calculate_weekly_mileage(40, "Marathon", 12, experience_level)
        assert len(result) == 12
        assert all(week > 0 for week in result)
    
    @pytest.mark.parametrize("race_distance", [
        "5K", "10K", "Half Marathon", "Marathon"
    ])
    def test_all_race_distances(self, race_distance):
        """Test that all race distances produce valid plans"""
        result = calculate_weekly_mileage(30, race_distance, 8, "Intermediate")
        assert len(result) == 8
        assert all(week > 0 for week in result)


class TestIntegration:
    """Integration tests combining multiple functions"""

    @patch("plan_generator.datetime")
    def test_full_training_plan_workflow(self, mock_datetime):
        """Test a complete training plan calculation workflow"""

        mock_datetime.now.return_value = datetime(2026, 1, 6)
        mock_datetime.strptime = datetime.strptime

        # 1️⃣ Calculate weeks until race
        weeks = calculate_weeks_until("2026-04-30")

        # 2️⃣ Calculate target pace (string πλέον)
        pace = calculate_pace(180, "Half Marathon")

        # 3️⃣ Get run types
        run_types = calculate_weekly_type_of_runs("5 days")

        # 4️⃣ Generate mileage plan
        mileage = calculate_weekly_mileage(
            weekly_distance=20,
            race_distance="10K",
            weeks_until=weeks,
            experiencelevel="Beginner"
        )

        # ✅ Assertions (domain-based, όχι fragile)

        assert weeks >= 14
        assert weeks <= 18

        assert isinstance(pace, str)
        assert ":" in pace   # π.χ. "8:32"

        assert len(run_types) == 5
        assert "long" in run_types

        assert len(mileage) == weeks
        assert mileage[0] > 0
        assert max(mileage) > mileage[0]   # progression
        assert mileage[-1] < mileage[-2]   # taper