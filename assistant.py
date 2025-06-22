import speech_recognition as sr
import pyttsx3
import json

# Initialize TTS and recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        speak("Sorry, I didn’t catch that.")
        return ""

# Load recipes from file
with open("recipes.json") as file:
    recipes = json.load(file)

# Ask user what they want to cook
speak("What would you like to cook today? For example, pasta or tea.")
chosen = listen()

# Match recipe
if chosen in recipes:
    steps = recipes[chosen]
    speak(f"Great! Let's start making {chosen}.")
    step = 0
    while step < len(steps):
        speak(f"Step {step + 1}: {steps[step]}")
        speak("Say 'next' or 'repeat'.")
        command = listen()

        if "next" in command:
            step += 1
        elif "repeat" in command:
            continue
        elif "stop" in command or "exit" in command:
            speak("Okay, stopping the assistant.")
            break
        else:
            speak("Say 'next', 'repeat' or 'stop'.")
    if step >= len(steps):
        speak(f"{chosen.capitalize()} is ready! Enjoy your meal.")
else:
    speak("Sorry, I don't know that recipe yet.")
