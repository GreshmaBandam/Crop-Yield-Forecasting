import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Crop Yield Prediction", page_icon="🌾")
st.title("🌾 Crop Yield Prediction System")

st.write("Predict crop yield based on historical, climatic, and agricultural data.")

# -------------------------------
# Inputs
# -------------------------------
row_id = st.number_input(
    "Record Index (Unnamed: 0)",
    min_value=0,
    step=1,
    help="Dummy index value required by the trained model"
)

area = st.number_input(
    "Area (Encoded)",
    min_value=0,
    step=1
)

item = st.number_input(
    "Crop Type (Encoded)",
    min_value=0,
    step=1
)

year = st.number_input(
    "Year",
    min_value=1960,
    max_value=2035,
    step=1
)

rainfall = st.number_input(
    "Average Rainfall (mm/year)",
    min_value=0.0
)

pesticides = st.number_input(
    "Pesticides Used (tonnes)",
    min_value=0.0
)

temperature = st.number_input(
    "Average Temperature (°C)",
    min_value=-10.0,
    max_value=60.0
)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Yield"):
    try:
        input_df = pd.DataFrame(
            [[row_id, area, item, year, rainfall, pesticides, temperature]],
            columns=[
                "Unnamed: 0",
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

    except Exception as e:
        st.error("Prediction failed due to feature mismatch.")
        st.write(e)
