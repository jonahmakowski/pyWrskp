import speech_recognition as sr


def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('\b' * 14, "Listening...", end='', sep='')
        r.pause_threshold = 1
        audio = r.listen(source)

    print('\b' * 14, "Recognizing...", sep='')
    query = r.recognize_google(audio, language='en-in')

    return query
