
def compute_hourly_patterns(solar_ml, home_ml):
    
    solar_pattern = solar_ml.groupby("hour")["power"].mean()
    home_pattern = home_ml.groupby("hour")["usage"].mean()

    return solar_pattern, home_pattern


     

     

