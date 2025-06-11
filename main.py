import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

# === CONFIGURATION ===
API_KEY = "" # <-- Insert your OpenAI key here.
LANG = 'en' # gTTS language code
MIC_INDEX = 1 # Set your micphone device index

openai.api_key = API_KEY

WAKE_WORD = "hey pickles"
EXIT_WORD = "stop"

def get_audio():
    # Capture auto from the microphone and return it as text.
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=MIC_INDEX) as source:
        print("Listening") 
        audio = recognizer.listen(source)
    try:
        said = recognizer.recognize_google(audio)
        print(f"Me: {said}")
        return said.lower()
    except Exception as e:
        print(f"Speech recognition error: {e}")
        return ""

def respond(text):
    # Convert to speech and play it.
    tts = gTTS(text=text, lang=LANG, slow=False, tld="co.uk")
    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename) # clean up audio file

def main():
    print("Say 'Hey Pickles' to talk. Say 'stop' to exit.")
    while True:
        said = get_audio()
        if EXIT_WORD in said:
            print ("Exiting. Goodbye Peasant.")
            break
        if WAKE_WORD in said:
            # Remove the WAKE_WORD from the command
            command = said.split(WAKE_WORD, 1)[-1].strip()
            print(f"Command: {command}")
            try:
                response = openai.ChatCompletion. create (
                    model = "gpt-3.5-turbo",
                    message=[{"role": "user", "content": command}]
                )
                reply = response.choice[0].message.content
                print(f"Pickles: {reply}")
                respond(reply)
            except Exception as e:
                print(f"OpenAI error: {e}")

if __name__ == "__main__"
    main()
