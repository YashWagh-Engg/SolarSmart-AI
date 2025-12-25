print(">>> recommendations.py loaded")

def generate_recommendations(solar_pattern, home_pattern):
    # Normalize
    solar_norm = (solar_pattern - solar_pattern.min()) / (solar_pattern.max() - solar_pattern.min())
    home_norm = (home_pattern - home_pattern.min()) / (home_pattern.max() - home_pattern.min())

    # Opportunity score
    opportunity = solar_norm - home_norm

    # Best hours
    best_hours = opportunity.sort_values(ascending=False)
   
    return opportunity, best_hours
 