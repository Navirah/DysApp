from gtts import gTTS 
import os
file = open("result.txt", "r").read().replace("\n", " ")
speech = gTTS(text = str(file), slow = False)
speech.save('audio.mp3')
os.system('start audio.mp3')
