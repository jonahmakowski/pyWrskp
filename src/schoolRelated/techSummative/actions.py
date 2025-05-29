from datetime import datetime
import helper
import spotify
import weather_get


def get_time(prompt: str) -> str:
    """
    Get the current time in a formatted string.

    Returns:
        str: The current time in the format "HH:MM AM/PM".
    """
    time = datetime.now().strftime("%I:%M %p")
    helper.speak(f"The current time is {time}")


def play_song(prompt: str) -> None:
    """
    Play a song using the Spotify API.

    Args:
        prompt (str): The command to play a song.
    """
    song_name = (
        prompt.replace("play", "")
        .replace(".", "")
        .replace("!", "")
        .replace("?", "")
        .replace(",", "")
        .strip()
    )
    if song_name:
        spotify.play_song(song_name)
    else:
        helper.speak("Please specify a song to play.")


def daily_average_temperature(prompt: str) -> None:
    """
    Provides the average temperature for the current day by retrieving weather data.

    Args:
        prompt (str): A string prompt, typically used for initiating the function.

    Returns:
        None: This function does not return a value. It speaks the average temperature
        for the current day using the helper.speak function.

    Note:
        - The function retrieves weather data using the `weather_get.get_weather()` method.
        - The average temperature is extracted from the data for the current date.
        - The temperature is announced in degrees Celsius.
    """
    data = weather_get.get_weather()
    today = datetime.now().strftime("%Y-%m-%d")
    helper.speak(
        f"Today's average temperature is {round(data[today]['daily_avg_temp'], 1)} degrees Celsius."
    )
