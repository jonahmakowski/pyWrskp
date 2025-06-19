import requests
from datetime import datetime


def get_weather_forecast(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability,weathercode&current_weather=true&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None


def parse_forecast(data):
    # Check if the required keys are present
    if "daily" not in data:
        print("Error: 'daily' key not found in the API response.")
        return None
    elif "hourly" not in data:
        print("Error: 'hourly' key not found in the API response.")
        return None
    elif "current_weather" not in data:
        print("Error: 'current_weather' key not found in the API response.")
        return None

    daily_data = data["daily"]
    hourly_data = data["hourly"]
    current_data = data["current_weather"]

    # Extracting daily low and high temperatures
    daily_temps = daily_data["temperature_2m_max"]
    daily_low_temps = daily_data["temperature_2m_min"]
    daily_times = daily_data["time"]

    # Extracting hourly precipitation probability and temperature
    hourly_times = hourly_data["time"]
    hourly_precipitation = hourly_data["precipitation_probability"]
    hourly_temperatures = hourly_data["temperature_2m"]

    # Group hourly data by day
    daily_precipitation = [0] * 7
    daily_avg_temp = [0] * 7
    for idx, time in enumerate(hourly_times):
        day_idx = daily_times.index(time.split("T")[0])
        daily_precipitation[day_idx] = max(
            daily_precipitation[day_idx], hourly_precipitation[idx]
        )
        daily_avg_temp[day_idx] += hourly_temperatures[idx]

    # Calculate average temperature for each day
    daily_avg_temp = [temp / 24 for temp in daily_avg_temp]

    # Current weather condition
    current_temp = current_data["temperature"]
    current_weather_code = current_data["weathercode"]

    return (
        daily_times,
        daily_temps,
        daily_low_temps,
        daily_precipitation,
        daily_avg_temp,
        current_temp,
        current_weather_code,
    )


def weather_code_to_description(code):
    weather_conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return weather_conditions.get(code, "Unknown weather code")


def get_weather():
    latitude = "45.40805405383296"
    longitude = "-75.6875845660986"

    data = get_weather_forecast(latitude, longitude)
    data_out = {}
    if data:
        forecast_data = parse_forecast(data)
        if forecast_data:
            (
                daily_times,
                daily_temps,
                daily_low_temps,
                daily_precipitation,
                daily_avg_temp,
                current_temp,
                current_weather_code,
            ) = forecast_data
            for index, day in enumerate(daily_times):
                data_out[day] = {
                    "daily_temps": daily_temps[index],
                    "daily_low_temps": daily_low_temps[index],
                    "daily_precipitation": daily_precipitation[index],
                    "daily_avg_temp": daily_avg_temp[index],
                }
            data_out["current_temp"] = current_temp
            data_out["current_weather"] = weather_code_to_description(
                current_weather_code
            )

    return data_out


if __name__ == "__main__":
    print(get_weather())
