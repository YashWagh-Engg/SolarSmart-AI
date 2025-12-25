import pandas as pd

def load_solar_data(path):
    solar_df = pd.read_csv(path)

    solar_df["DATE_TIME"] = pd.to_datetime(solar_df["DATE_TIME"])
    solar_df.set_index("DATE_TIME", inplace=True)

    solar_hourly = solar_df["AC_POWER"].resample("H").mean()
    return solar_hourly


def load_home_data(path):
    home_df = pd.read_csv(
        path,
        sep=";",
        na_values="?"
    )

    home_df["datetime"] = pd.to_datetime(
        home_df["Date"] + " " + home_df["Time"],
        dayfirst=True
    )
    home_df.set_index("datetime", inplace=True)

    home_df["Global_active_power"] = pd.to_numeric(
        home_df["Global_active_power"],
        errors="coerce"
    )

    home_hourly = home_df["Global_active_power"].resample("H").mean()
    return home_hourly
