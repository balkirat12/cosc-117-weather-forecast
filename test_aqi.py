from backend import calc_aqi_level
from config import AQI_INTERVALS

def test_so2_level_calculation():
    concentration = "77"
    intervals = AQI_INTERVALS["so2"]
    expected_level = 2  
    calculated_level = calc_aqi_level(concentration, intervals)
    assert calculated_level == expected_level

def test_co_level_calculation():
    concentration = "684.85"
    intervals = AQI_INTERVALS["co"]
    expected_level = 2  
    calculated_level = calc_aqi_level(concentration, intervals)
    assert calculated_level == expected_level
