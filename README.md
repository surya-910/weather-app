# Weather App with Live OpenWeather API

## Project Description
A beginner-friendly Python application that fetches and displays real-time weather information for any city using the OpenWeather API.

## Features
- Get live weather information.
- Search weather by city name.
- Display temperature in Celsius.
- Show feels-like temperature.
- Display weather conditions.
- Show humidity and wind speed.
- Handle API errors and connection issues.

## Technologies Used
- Python 3
- Requests Library
- OpenWeather API

## Installation

Install the required library:

```bash
pip install requests
```

## API Key Setup

1. Create an API key at [OpenWeather](https://openweathermap.org/api).
2. Set your API key as an environment variable in PowerShell:

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

**Note:** Replace `YOUR_API_KEY` with your own key. Never upload your actual API key to GitHub.

## How to Run

Run the following command:

```bash
python weather_app.py
```

Enter a city name to view its current weather details.

## Sample Output

```text
========== WEATHER DETAILS ==========
City: Chennai
Temperature: 33.79 C
Weather: broken clouds
Humidity: 58 %
Wind Speed: 4.42 m/s
=====================================
```

## Learning Outcomes
- Understanding API integration.
- Sending HTTP requests using Python.
- Handling JSON responses.
- Working with environment variables.
- Handling errors and exceptions.

## Project Status
Completed
