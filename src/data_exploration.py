import pandas as pd
import matplotlib.pyplot as plt

# ---------- SOLAR DATA ----------
solar_df = pd.read_csv("data/solar_power_generation.csv")

# Convert timestamp
solar_df["DATE_TIME"] = pd.to_datetime(solar_df["DATE_TIME"])

# Set timestamp as index
solar_df.set_index("DATE_TIME", inplace=True)

# Keep only power column
solar_hourly = solar_df["AC_POWER"].resample("H").mean()

print("Solar hourly data:")
print(solar_hourly.head())

# ---------- HOME CONSUMPTION DATA ----------
home_df = pd.read_csv(
    "data/household_power_consumption.csv",
    sep=";",              # important for UCI dataset
    na_values="?"
)

# Combine Date + Time into one column
home_df["datetime"] = pd.to_datetime(
    home_df["Date"] + " " + home_df["Time"],
    dayfirst=True
)

home_df.set_index("datetime", inplace=True)

# Convert power to numeric
home_df["Global_active_power"] = pd.to_numeric(
    home_df["Global_active_power"],
    errors="coerce"
)

# Resample to hourly
home_hourly = home_df["Global_active_power"].resample("H").mean()

print("\nHome hourly data:")
print(home_hourly.head())

solar_hourly.iloc[:48].plot(title="Hourly Solar Generation")
plt.show()

home_hourly.iloc[:48].plot(title="Hourly Home Consumption")
plt.show()

#Day 2:

solar_ml = solar_hourly.reset_index()
solar_ml.columns = ["datetime","power"]

solar_ml = solar_hourly.reset_index()
solar_ml.columns = ["datetime", "power"]

solar_ml["hour"] = solar_ml["datetime"].dt.hour
solar_ml["day"] = solar_ml["datetime"].dt.day
solar_ml["month"] = solar_ml["datetime"].dt.month
solar_ml["dayofweek"] = solar_ml["datetime"].dt.dayofweek

solar_ml.dropna(inplace=True)

print("COLUMNS IN solar_ml:")
print(solar_ml.columns.tolist())

print(solar_ml.head())

from sklearn.model_selection import train_test_split # pyright: ignore[reportMissingModuleSource]

X = solar_ml[["hour","day","month","dayofweek"]]
y = solar_ml["power"]

X_train, X_test, y_train, y_test = train_test_split(  # pyright: ignore[reportUndefinedVariable]
    X, y, test_size=0.2, shuffle=False
)

from sklearn.ensemble import RandomForestRegressor # pyright: ignore[reportMissingModuleSource]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train) # pyright: ignore[reportUndefinedVariable]

from sklearn.metrics import mean_absolute_error # pyright: ignore[reportMissingModuleSource]

predictions = model.predict(X_test) # pyright: ignore[reportUndefinedVariable]
mae = mean_absolute_error(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f}")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))
plt.plot(y_test.values[:48], label="Actual")
plt.plot(predictions[:48], label="Predicted")
plt.legend()
plt.title("Solar Power: Actual vs Predicted (Sample)")
plt.show()

# Day 3:

home_ml = home_hourly.reset_index()
home_ml.columns = ["datetime", "consumption"]

home_ml["hour"] = home_ml["datetime"].dt.hour
home_ml["day"] = home_ml["datetime"].dt.day
home_ml["month"] = home_ml["datetime"].dt.month
home_ml["dayofweek"] = home_ml["datetime"].dt.dayofweek

home_ml.dropna(inplace=True)

print("HOME_ML COLUMNS:")
print(home_ml.columns.tolist())

print(home_ml.head())

home_ml.rename(columns={home_ml.columns[1]: "usage"}, inplace=True)

peak_threshold = home_ml["usage"].quantile(0.80)

home_ml["is_peak"] = home_ml["usage"] >= peak_threshold
print("Peak threshold:",peak_threshold)
print(home_ml["is_peak"].value_counts())

peak_by_hour = home_ml.groupby("hour")["is_peak"].mean()
print("\nPeak probability by hour:")
print(peak_by_hour)

peak_by_hour.plot(kind="bar", title="Probability of Peak Usage by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Peak Probability")
plt.show()

#Day 4:

solar_pattern =  solar_ml.groupby("hour")["power"].mean()

home_pattern = home_ml.groupby("hour")["usage"].mean()

print("\nAverage solar by Hour:")
print(solar_pattern)
print("\nAverage home usage Hour:")
print(home_pattern)

solar_norm = (solar_pattern - solar_pattern.min()) / (solar_pattern.max() - solar_pattern.min())
home_norm = (home_pattern - home_pattern.min()) / (home_pattern.max() - home_pattern.min())

opportunity = solar_norm - home_norm 

best_hours = opportunity.sort_values(ascending= False) 
print("\nBest hours to use heavy application")
print(best_hours.head(5))

print("\n-----RECOMMENDATIONS-----")
for hour in best_hours.head(3).index:
    print(f"Try to run heavy application around {hour}:00 hrs")

opportunity.plot(kind="bar", title="Solar Opportunity Score by Hour") 
plt.xlabel("Hour of Day")
plt.ylabel("Opportunity Score (Higher = Better)")
plt.show()

