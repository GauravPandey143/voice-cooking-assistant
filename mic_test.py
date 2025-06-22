import speech_recognition as sr

mic_list = sr.Microphone.list_microphone_names()
print("Microphones available:")
for i, mic in enumerate(mic_list):
    print(f"{i}: {mic}")
