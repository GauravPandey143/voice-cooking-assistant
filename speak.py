import pyttsx3

# Start the voice engine
engine = pyttsx3.init()

# What you want it to say
text = "Welcome to your cooking assistant! Let's make something delicious and healthy"

# Speak it
engine.say(text)
engine.runAndWait()
