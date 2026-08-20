# Weather Report App
Python CLI application that fetches real-time weather information for any city using the OpenWeatherMap API.

## Getting Started

### Prerequisites
Python 3.10.0
git

### Installation
1. Clone repository  
    git clone https://github.com/colbyrobbins/weather-report-app.git
2. Create and activate venv  
    python -m venv .venv  
    .venv\Scripts\activate.ps1
3. Install dependencies  
    pip install requests, python-dotenv, streamlit  
4. Configure environment variables  
    code .env  
    OPENWEATHER_API_KEY=your_api_key

### Usage
streamlit run streamlit_app.py
