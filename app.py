import streamlit as st
import pickle
import pandas as pd

# -------------------------------
# Load trained model
# -------------------------------
model = pickle.load(open("model.pkl", "rb"))

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Crop Yield Prediction System")
st.write("Enter the details below to predict crop yield (hg/ha)")

# -------------------------------
# User Inputs
# -------------------------------
area = st.number_input(
    "Area (Encoded Value)",
    min_value=0,
    step=1,
    help="Encoded value of country/region used during training"
)

item = st.number_input(
    "Crop Type (Encoded Value)",
    min_value=0,
    step=1,
    help="Encoded value of crop type used during training"
)

year = st.number_input(
    "Year",
    min_value=1960,
    max_value=2030,
    step=1
)

rainfall = st.number_input(
    "Average Rainfall (mm per year)",
    min_value=0.0,
    help="Typical range: 500 – 2000 mm"
)

pesticides = st.number_input(
    "Pesticide Usage (tonnes)",
    min_value=0.0
)

temperature = st.number_input(
    "Average Temperature (°C)",
    min_value=-5.0,
    max_value=60.0,
    help="Typical range: 10 – 35 °C"
)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Yield"):
    try:
        # Create DataFrame with EXACT feature names used in training
        input_df = pd.DataFrame(
            [[area, item, year, rainfall, pesticides, temperature]],
            columns=[
                "Area",
                "Item",
                "Year",
                "average_rain_fall_mm_per_year",
                "pesticides_tonnes",
                "avg_temp"
            ]
        )

        prediction = model.predict(input_df)

        st.success(f"🌱 Predicted Crop Yield: **{prediction[0]:.2f} hg/ha**")

        # -------------------------------
        # Simple Recommendations
        # -------------------------------
        if rainfall < 500:
            st.warning("⚠️ Low rainfall detected. Consider additional irrigation.")
        if temperature > 35:
            st.warning("⚠️ High temperature may affect yield. Heat-resistant crops recommended.")
        if pesticides > 150:
            st.warning("⚠️ High pesticide usage detected. Optimize pesticide application.")

    except Exception as e:
        st.error("An error occurred during prediction.")
        st.write(e)
