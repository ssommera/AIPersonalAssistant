import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr


api_key = ""
lang = 'en'

openai.api_key = api_key

person = ""

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global person
                person = said

                if "Hey Pickles" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    print(new_string)
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="co.uk") # <-- is the British accent, and com.au is the Australian one.
                    speech.save("hi1.mp3")
                    playsound.playsound("hi1.mp3")

            except Exception:
                print("Exception")

        return said


    if "stop" in person:
        break

    get_audio()
