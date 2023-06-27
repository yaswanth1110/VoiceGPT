import pyttsx3
import openai
import os
import speech_recognition as sr
openai.api_key = "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"
os.system("color a")
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message
def take_c():
    r = sr.Recognizer()
    with sr.Microphone() as s:
        speak('Listening'),print('listening')
        r.pause_threshold = 0.7
        audio = r.listen(s)
        try:
            speak("Recognizing"),print("Recognizing")
            Query = r.recognize_google(audio)
        except Exception as e:
            print(e)
            print(" Say Again sir"),speak("sir i cannot hear you sir Say Again sir")
            return ""
        return Query
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
if __name__ == '__main__':
    while True:
        c=take_c()
        b=generate_text(c)
        speak(b)
        
