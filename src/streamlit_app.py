import requests
import os
from dotenv import load_dotenv
import streamlit as st
import re

load_dotenv()
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = None
try:
    if "OPENWEATHER_API_KEY" in st.secrets:
        API_KEY = st.secrets["OPENWEATHER_API_KEY"]
except (FileNotFoundError, Exception):
    pass

if not API_KEY:
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_emoji(description):
    desc = description.lower()

    if re.search(r"thunder|storm|lightning", desc):
        return "⚡"
    elif re.search(r"rain|drizzle|shower", desc):
        return "🌧️"
    elif re.search(r"snow|ice|blizzard|flurry", desc):
        return "❄️"
    elif re.search(r"cloud|overcast", desc):
        return "☁️"
    elif re.search(r"sun|clear", desc):
        return "☀️"
    else:
        return "🌡️"

def display_weather(name, temp, humidity, description):
    emoji = get_weather_emoji(description)

    card_html = f"""
    <div style="background-color: #1e3a8a; color: white; padding: 20px; border-radius: 12px; text-align: center;">
        <h2>{name}</h2>
        <p style="font-size: 1.2rem;">
            {emoji} {description.title()} &nbsp;|&nbsp; 
            🌡️ {temp}°C &nbsp;|&nbsp; 
            💧 {humidity}%
        </p>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

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

    display_weather(name, temp, humidity, description)

if __name__ == "__main__":
    st.title("Weather Report App")
    city = st.text_input("Enter city name:")
    if st.button("Get Weather"):
        if city:
            get_weather(city)
        else:
            st.error("Please enter a city name.")
