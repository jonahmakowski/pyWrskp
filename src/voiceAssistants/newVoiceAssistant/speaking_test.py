import pyttsx3


def test_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    for voice in voices:
        engine.setProperty("voice", voice.id)
        # Check if the voice language is English
        if "en" in voice.languages[0].decode("utf-8").lower():
            print(f"Testing voice: {voice.name}")
            engine.say("Hello, world!")
            engine.runAndWait()


if __name__ == "__main__":
    test_voices()
