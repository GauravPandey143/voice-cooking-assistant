import speech_recognition as sr

# Create recognizer
recognizer = sr.Recognizer()

# Use your microphone as input
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

try:
    # Recognize what you said using Google
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand that.")
except sr.RequestError:
    print("Could not request results, check your internet.")
