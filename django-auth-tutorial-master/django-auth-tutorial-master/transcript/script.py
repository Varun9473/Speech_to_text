import speech_recognition as sr

r=sr.Recognizer()
var=sr.AudioFile('file1.wav')
with var as source:
    audio = r.record(source)

print(r.recognize_google(audio))

