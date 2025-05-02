from pyWrkspPackage import list_to_str, ai_response, load_from_file
from helper import *
import actions
from os import getenv
from dotenv import load_dotenv
import pvporcupine
from pvrecorder import PvRecorder
import speech_recognition as sr
from datetime import datetime
from pandas.io.clipboard import paste
import spotify
from weather_get import get_weather
from google_calendar import get_events, get_credentials, do_make_event

# General Setup
load_dotenv()
AI_KEY = getenv("AI_TOKEN")
VOICE_KEY = getenv("VOICE_DETECTION_TOKEN")
AI_MODEL = getenv("AI_MODEL")
AI_URL = getenv("AI_URL")
SYS_PROMPT = load_from_file("prompt.md")
# Commands dictionary format: {ai_command: [function, requires_arguments, gets_prompt_as_argument]}
COMMANDS = {
    "open-app": [actions.open_app, True],
    "search-the-web": [actions.search, True],
    "open-file": [actions.open_file, True],
    "spotify": [spotify.do_spotify, True, True],
    "open-webpage": [actions.open_webpage, True],
    "open-folder": [actions.open_directory_in_finder, True],
    "hide-application": [actions.hide_app, True],
    "question-mode": ["Question Mode", False],
    "clipboard-contents": [paste, False],
    "terminate": [actions.terminate, False],
    "quit-application": [actions.quit_app, True],
    "make-event": [do_make_event, True, True],
}
USER_NAME = "Jonah"

# Verify google calendar credentials
get_credentials()

# Confirming env variables are set
if AI_KEY is None or VOICE_KEY is None:
    raise ValueError(
        "An environment variable (AI_KEY or VOICE_DETECTION_TOKEN) is not set"
    )


def get_sys_prompt() -> str:
    """
    Generates a system prompt string containing the current date, time, user name, AI model,
    and formatted weather information.

    Returns:
        str: A formatted system prompt string.

    Dependencies:
        - datetime.now(): Retrieves the current date and time.
        - get_weather(): Fetches weather data.
        - ai_weather_display(weather_data): Formats the weather data for display.
        - SYS_PROMPT: A predefined string template requiring placeholders for date, time,
          user name, AI model, and weather information.
        - USER_NAME: The name of the user.
        - AI_MODEL: The name or identifier of the AI model.
    """
    current_datetime = datetime.now()
    cur_date = current_datetime.strftime("%B %d, %Y")
    cur_time = current_datetime.strftime("%I:%M %p")
    weather_data = get_weather()
    weather_display = ai_weather_display(weather_data)
    _, events = get_events(5)
    return SYS_PROMPT.format(
        cur_date, cur_time, USER_NAME, AI_MODEL, weather_display, events
    )


# Define Functions
def get_message_list(cur_list: list, message: str, max_size=10) -> list:
    """
    Update the message list with a new user message.

    Args:
        cur_list (list): The current list of messages.
        message (str): The new user message to add.
        max_size (int, optional): The maximum size of the message list. Defaults to 10.

    Returns:
        list: The updated message list.
    """
    if not cur_list:
        return [
            {"role": "system", "content": get_sys_prompt()},
            {"role": "user", "content": message},
        ]
    while len(cur_list) > max_size:
        cur_list.pop(0)
    cur_list[0] = {"role": "system", "content": get_sys_prompt()}
    cur_list.append({"role": "user", "content": message})
    return cur_list


def parse_command(message: str, message_list: list) -> tuple[str, bool]:
    """
    Parses a given message to identify and execute commands, and returns the processed message
    along with a flag indicating whether the message is in "Question Mode".

    Args:
        message (str): The input message to be parsed.
        message_list (list): A list of previous messages for context or processing.

    Returns:
        tuple[str, bool]: A tuple containing:
            - The processed message as a string.
            - A boolean indicating whether the message is in "Question Mode".

    Behavior:
        - Splits the input message by the '$' delimiter.
        - Searches for predefined commands in the split message chunks.
        - Executes the corresponding function for the identified command, if any.
        - Handles specific cases such as "Question Mode" and clipboard operations.
        - If no command is identified, returns the original message and a flag indicating
          whether the message contains a '?' character.
    """
    split_message = message.split("$")
    command = None
    for chunk in split_message:
        for key in COMMANDS.keys():
            if key in chunk:
                del split_message[split_message.index(chunk)]
                command = (COMMANDS[key], chunk)
                break

    if command is None:
        return message, "?" in message

    func = command[0][0]
    if func == "Question Mode":
        return list_to_str(split_message), True
    elif len(command[0]) == 3:
        func(list_to_str(split_message))
    elif func == paste:
        print("Ran command {} without arguments".format(key))
        speak(command[1].split()[0])
        clipboard = str(paste())
        print(clipboard)
        message_list = get_message_list(
            message_list, "AUTOMATED RESPONSE: Clipboard contents: {}".format(clipboard)
        )
        print(message_list)
        response, message_list = ai_response(
            message_list, AI_MODEL, AI_URL, AI_KEY, stream=False
        )
        return response, False
    elif command[0][1]:
        print(
            'Ran command {} with arguments "{}"'.format(
                key, list_to_str(command[1].split()[1:], sep=" ")
            )
        )
        func(list_to_str(command[1].split()[1:], sep=" "))
    else:
        print("Ran command {} without arguments".format(key))
        func()

    return list_to_str(split_message), False


# Running the actual assistant code
def main():
    """
    Main function to initialize and run the voice assistant.

    This function sets up the Porcupine wake word detection engine and the PvRecorder
    for audio input. It listens for a wake word ("computer") and processes voice commands
    to interact with an AI model. The assistant can respond to user queries and execute
    specific actions based on the parsed commands.

    Workflow:
    1. Initializes the Porcupine engine with the specified wake word.
    2. Starts the PvRecorder to capture audio input.
    3. Plays a bootup sound to indicate readiness.
    4. Continuously listens for the wake word or processes commands in question mode.
    5. Adjusts system volume during command processing to avoid interference.
    6. Sends user input to an AI model for generating responses.
    7. Parses the AI response to determine actions and replies.
    8. Handles cleanup and resource deallocation on exit.

    Exceptions:
    - Handles `KeyboardInterrupt` to allow graceful termination.
    - Handles `sr.UnknownValueError` to skip unrecognized audio input.

    Note:
    - Requires valid `VOICE_KEY`, `AI_MODEL`, `AI_URL`, and `AI_KEY` for functionality.
    - Assumes the existence of helper functions like `play_sound`, `take_command`,
        `get_message_list`, `ai_response`, `parse_command`, `speak`, and `actions`.

    """
    porcupine = pvporcupine.create(access_key=VOICE_KEY, keywords=["computer"])
    recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    message_list = []
    question_mode = False

    play_sound(True, "audio/bootup.mp3")

    try:
        recoder.start()
        while True:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0 or question_mode:
                recoder.stop()
                prev_volume = actions.get_current_volume()
                play_sound(True)
                actions.set_volume(0)
                try:
                    inp = take_command()
                except sr.UnknownValueError:
                    recoder.start()
                    continue
                actions.set_volume(prev_volume)

                message_list = get_message_list(message_list, inp)
                message, message_list = ai_response(
                    message_list, AI_MODEL, AI_URL, AI_KEY
                )
                print(message)
                speak_version, question_mode = parse_command(message, message_list)

                speak(speak_version)

                recoder.start()

    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()


if __name__ == "__main__":
    main()
