print(">>> main.py started")

from data_processing import load_solar_data, load_home_data
from patterns import compute_hourly_patterns
from recommendation import generate_recommendations

solar_hourly = load_solar_data("data/solar_power_generation.csv")
home_hourly = load_home_data("data/household_power_consumption.csv")

# --- Feature engineering for solar ---
solar_ml = solar_hourly.reset_index()
solar_ml.columns = ["datetime", "power"]

solar_ml["hour"] = solar_ml["datetime"].dt.hour
solar_ml["day"] = solar_ml["datetime"].dt.day
solar_ml["month"] = solar_ml["datetime"].dt.month
solar_ml["dayofweek"] = solar_ml["datetime"].dt.dayofweek

# --- Feature engineering for home ---
home_ml = home_hourly.reset_index()
home_ml.columns = ["datetime", "usage"]

home_ml["hour"] = home_ml["datetime"].dt.hour
home_ml["day"] = home_ml["datetime"].dt.day
home_ml["month"] = home_ml["datetime"].dt.month
home_ml["dayofweek"] = home_ml["datetime"].dt.dayofweek

solar_pattern, home_pattern = compute_hourly_patterns(solar_ml, home_ml)

opportunity, best_hours = generate_recommendations(solar_pattern, home_pattern)


print(solar_hourly.head())
print(home_hourly.head())


