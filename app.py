import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

st.title("🌾 Crop Yield Prediction System")
st.write("Enter the details below to predict crop yield (hg/ha)")

# ---- User Inputs ----
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
    help="Encoded value of crop used during training"
)

year = st.number_input(
    "Year",
    min_value=1960,
    max_value=2030,
    step=1
)

rainfall = st.number_input(
    "Average Rainfall (mm per year)",
    min_value=0.0
)

pesticides = st.number_input(
    "Pesticide Usage (tonnes)",
    min_value=0.0
)

temperature = st.number_input(
    "Average Temperature (°C)"
)

# ---- Prediction ----
if st.button("Predict Yield"):
    input_data = np.array([[area, item, year, rainfall, pesticides, temperature]])
    prediction = model.predict(input_data)

    st.success(f"🌱 Predicted Crop Yield: **{prediction[0]:.2f} hg/ha**")

    # ---- Simple Recommendations ----
    if rainfall < 500:
        st.warning("⚠️ Low rainfall detected. Consider additional irrigation.")
    if temperature > 35:
        st.warning("⚠️ High temperature may reduce yield. Heat-resistant crops recommended.")
