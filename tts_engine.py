import pyttsx3

def text_to_speech(text: str, output_file="tts.wav"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    engine.setProperty("volume", 1.0)

    engine.save_to_file(text, output_file)
    engine.runAndWait()
