import speech_recognition as sr
import os
from  gtts  import  gTTS
import playsound
import threading 
import time
import random
import wikipedia
listener = sr.Recognizer() 

x=1
print(random)
def sat(texts):
	ran = random.randint(1,1000000)
	tts= gTTS(texts,lang='en')
	tts.save(f"audio-{ran}.mp3")
	playsound.playsound(f"audio-{ran}.mp3")
	os.remove(f"audio-{ran}.mp3")


def play(dir):
	if 'jarvis wake up' in dir.lower():
		sat('i am online and ready sir')
	if 'who made you' in dir.lower():
		sat('i was designed, programmed and deployed by hacker anania')
	if 'jarvis' in dir.lower():
		sat('what can i help you anania')
	if  "what's" in str(dir.lower()):
		try:
			x = dir.replace("what's",'')
			ny = wikipedia.set_lang('en')
			word=wikipedia.summary(str(x), sentences=1)
			sat(f'according to wikipedia.org {word}')
		except:
			pass	

	if  "shutdown" in dir.lower():
		sat('good bye sir')
		os.system('shutdown /s ')	

while True:
	with sr.Microphone() as source:
		if x == 1:
			#sat('ready sir')
			print('ready ...')
			x=0
			threading.Thread(target=sat('ready sir'))
		else:
			pass	
		listener.adjust_for_ambient_noise(source, duration=1)
		voice = listener.listen(source)
		try:
			command =listener.recognize_google(voice)
			print(command)
			play(command)
		except:
			pass	