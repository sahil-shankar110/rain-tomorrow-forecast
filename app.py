import streamlit as st
from src.weather_api import get_current_weather
from src.data_utils import prepare_live_data
from src.predictor import load_model, predict_rain
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Rain-Forecasting Predictor", page_icon="🌧️", layout="wide")

st.title("🌧️ Rain Tomorrow Prediction System")
# st.markdown("**Machine Learning–powered live weather prediction**")

model, le_wind = load_model()

col1, col2 = st.columns([2, 1])

with col1:
    st.header("🔍 Live Prediction")
    city = st.text_input("Enter city name", placeholder="e.g. London, Karachi, Tokyo")

    if st.button("🚀 Predict Weather"):
        with st.spinner("Fetching live weather data..."):
            weather = get_current_weather(city)

            if not weather:
                st.error("City not found or invalid input.")
            else:
                st.metric("🌡 Temperature", f"{weather['Temp']:.1f} °C")
                st.metric("💧 Humidity", f"{weather['Humidity']} %")
                st.metric("💨 Wind Speed", f"{weather['WindGustSpeed']:.1f} km/h")

                input_data = prepare_live_data(weather, le_wind)
                pred, conf = predict_rain(model, input_data)

                if pred == 1:
                    st.error("🌧️ Rain expected tomorrow")
                else:
                    st.success("☀️ No rain expected tomorrow")

                st.info(f"Model Confidence: {conf:.1f}%")

with col2:
    st.header("📊 Model Details")
    st.success("RandomForestClassifier")
    st.info("Accuracy: 83.5%")
    st.markdown("""
    **Features Used**
    - Temperature (Min, Max, Current)
    - Humidity
    - Atmospheric Pressure
    - Wind Speed & Direction
    """)

st.markdown("---")
st.caption("Built using Streamlit • OpenWeatherMap API • Machine Learning Concepts")
