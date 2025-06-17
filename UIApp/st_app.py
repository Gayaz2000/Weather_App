import streamlit as st
import requests

st.title("🔗 Weather App")

city = st.text_area("Enter your prompt")
WEATHER_API_KEY = st.text_input("Enter your openweather api key", type="password") #type="password"

if st.button("Get Weather"):
    if city and WEATHER_API_KEY:
        with st.spinner("Waiting for LLM response..."):
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"city": city, "WEATHER_API_KEY":WEATHER_API_KEY}
            )
            if response.status_code == 200:
                result = response.json()["response"]
                st.success(result)
            else:
                st.error("Failed to get response from LLM.")
