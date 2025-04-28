from os import remove
import whisper
import pyttsx3
from pygame import mixer
from time import sleep
import speech_recognition as sr

# Setting up Audio Systems
mixer.init() # mp3 player init
engine = pyttsx3.init() # text to speech init
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
model = whisper.load_model('base.en') # Whisper model init

def take_command() -> str:
    """
    Listens for a voice command and returns the recognized text.

    This function uses the `speech_recognition` library to capture audio from the microphone,
    then processes the audio to recognize and return the spoken text.

    Returns:
        str: The recognized text from the audio input.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    print("Recognizing...")
    with open("temp_audio.wav", "wb") as f:
        f.write(audio.get_wav_data())
    transcription = model.transcribe("temp_audio.wav")['text']
    remove("temp_audio.wav")

    return transcription

def play_sound(hold: bool, sound='audio.mp3') -> None:
    """
    Play a sound file using the mixer module.

    Args:
        hold (bool): If True, the function will block until the sound finishes playing.
        sound (str, optional): The path to the sound file to play. Defaults to 'audio.mp3'.
    """
    mixer.music.load(sound)
    mixer.music.play()
    if hold:
        while mixer.music.get_busy():
            sleep(0.001)

def speak(message: str, voice=132, hold=True) -> None:
    """
    Convert text to speech and play it through the speakers.

    Args:
        message (str): The text message to be spoken.
        voice (int, optional): The index of the voice to use. Defaults to 132.
    """
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)  # Changing index changes voices
    engine.say(message)
    engine.runAndWait()

def ai_weather_display(data):
    """
    Formats and displays weather data in a readable string format.
    Args:
        data (dict): A dictionary containing weather information. 
                     Expected keys:
                     - 'current_temp' (str): The current temperature.
                     - 'current_weather' (str): The current weather condition.
                     - Other keys representing dates (str), where each date maps to a dictionary with:
                       - 'max_temp' (float): The maximum temperature for the date in °C.
                       - 'min_temp' (float): The minimum temperature for the date in °C.
                       - 'precipitation' (float): The precipitation percentage for the date.
                       - 'avg_temp' (float): The average temperature for the date in °C.
    Returns:
        str: A formatted string displaying the current weather and forecast details for each date.
    """
    out = f"Current Temperature: {data['current_temp']}\nCurrent Weather: {data['current_weather']}"
    for date in data:
        if not isinstance(data[date], dict):
            continue
        out += f"Date: {date}\n"
        out += f"Max Temp: {data[date]['daily_temps']}°C\n"
        out += f"Min Temp: {data[date]['daily_low_temps']}°C\n"
        out += f"Chance of Precipitation: {data[date]['daily_precipitation']}%\n"
        out += f"Avg Temp: {data[date]['daily_avg_temp']}°C\n"
        out += "\n"
    
    return out
