import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
API_KEY = st.secrets.get("OPENWEATHER_API_KEY") or os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    data = response.json()

    name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    st.write(f"Today's weather in {name}:")
    st.write(f"Temperature: {temp}°C")
    st.write(f"Humidity: {humidity}%")
    st.write(f"Description: {description}")

if __name__ == "__main__":
    st.title("Weather Report App")
    city = st.text_input("Enter city name:")
    if st.button("Get Weather"):
        if city:
            get_weather(city)
        else:
            st.error("Please enter a city name.")
