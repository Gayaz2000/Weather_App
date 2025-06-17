import streamlit as st
from weather_func import get_weather_from_weatherapi

import streamlit as st
import asyncio
import httpx

# Streamlit App UI
st.title("⛅⛈🌪 Weather App 🌩🌨☄")

city = st.text_input("Enter your city")
WEATHER_API_KEY = st.text_input("Enter your weather API Key", type="password")

if st.button("Run"):
    with st.spinner("Fetching weather data..."):
        if __name__ == "__main__":
            result = get_weather_from_weatherapi(city, WEATHER_API_KEY)
            #print("\n✅ Weather Report:\n")
            #print(result)
    st.write(result)
