import streamlit as st

from data_processing import load_solar_data, load_home_data
from patterns import compute_hourly_patterns
from recommendation import generate_recommendations

st.set_page_config(page_title="SolarSmart AI", layout="centered")

st.title(" SolarSmart AI")
st.markdown(
    """
**SolarSmart AI** helps rooftop solar users maximize their savings by:
- Analyzing solar generation patterns 🌞  
- Understanding home electricity usage 🏠  
- Recommending the best hours to run heavy appliances ⚡  

👉 Upload your data in the sidebar and click **Run Analysis** to get started.
"""
)
st.divider()

st.write("AI-powered recommendations to maximize rooftop solar savings.")

st.sidebar.header("Upload Data Files")

solar_file = st.sidebar.file_uploader(
    "Upload Solar Generation CSV", type=["csv"]
)

home_file = st.sidebar.file_uploader(
    "Upload Home Consumption CSV", type=["csv"]
)

if st.sidebar.button("Run Analysis"):
    if solar_file is None or home_file is None:
        st.error("Please upload both CSV files to continue.")
        st.stop()

    # rest of your logic...
    st.sidebar.header("Upload Data Files")

    st.info("Loading data and running analysis...")

    # Load data
    solar_hourly = load_solar_data(solar_file)
    home_hourly = load_home_data(home_file)

    # Feature engineering
    solar_ml = solar_hourly.reset_index()
    solar_ml.columns = ["datetime", "power"]
    solar_ml["hour"] = solar_ml["datetime"].dt.hour

    home_ml = home_hourly.reset_index()
    home_ml.columns = ["datetime", "usage"]
    home_ml["hour"] = home_ml["datetime"].dt.hour

    # Patterns
    solar_pattern, home_pattern = compute_hourly_patterns(solar_ml, home_ml)

    # Recommendations
    opportunity, best_hours = generate_recommendations(solar_pattern, home_pattern)

    st.success("Analysis completed!")

    # -------- UI Layout --------
    st.subheader("📊 Hourly Patterns")

    col1, col2 = st.columns(2)

    with col1:
        st.write("🌞 Average Solar Generation by Hour")
        st.line_chart(solar_pattern)

    with col2:
        st.write("🏠 Average Home Usage by Hour")
        st.line_chart(home_pattern)

    st.subheader("⚡ Solar Opportunity Score")
    st.bar_chart(opportunity)

    st.subheader("🔝 Best Hours to Use Heavy Appliances")
    top_hours = best_hours.head(3)

    st.subheader("🧠 How it works")
    st.markdown(
    """
1. **Hourly patterns** are learned from your data.  
2. Solar and home usage are normalized for fair comparison.  
3. An **opportunity score** is computed for each hour:
   > High solar − Low usage = Best time to shift load.  
4. Top hours are recommended to reduce grid usage and maximize solar benefit.
"""
)


    for i, hour in enumerate(top_hours.index, start=1):
        st.markdown(f"**{i}. {hour}:00 hrs** — Best time to run heavy loads")

    st.info(
        "💡 Tip: Try shifting flexible appliances (washing machine, water pump, EV charging) "
        "to these hours to maximize solar usage and reduce grid consumption."
    )

st.divider()
st.caption(" | SolarSmart AI")
