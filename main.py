import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import subprocess as subP
from gtts import gTTS
from time import ctime
listen = True
r = sr.Recognizer()

user_name = False
cpu_name = False



def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            cpu_talk(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            cpu_talk('Sorry, I did not understand you')
        except sr.RequestError:
            cpu_talk('Sorry, my server seems down at the moment!')
        return voice_data

def cpu_talk(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,100000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
    print(audio_string)

def respond(voice_data):
    if cpu_name and cpu_name in voice_data or 'hey computer' in voice_data:
        if 'what time is it' in voice_data:
            cpu_talk(ctime())
        elif 'search' in voice_data:
            search = record_audio('What do you want to search for?')
            url = 'https://google.com/search?q='+search
            webbrowser.get().open(url)
            cpu_talk('Here is what I could find for ' + search)
        else:
            info = record_audio(f'How can I help you today')
    if 'find location' in voice_data:
        location = record_audio('Please provide a location?')
        url = 'https://google.com/maps/place/'+location
        webbrowser.get().open(url)
        cpu_talk('Here is the requested location: '+location)
    if 'open site' in voice_data:
        theUrl = record_audio('What site would you like to visit?')
        webbrowser.get().open('http://'+theUrl)
        cpu_talk('Here\'s '+theUrl)
    if 'I need directions' in voice_data:
        from_data = record_audio('What is your starting point?')
        to_data = record_audio('What is your ending point?')
        webbrowser.get().open('https://google.com/maps/dir/'+from_data+'/'+to_data+'/')
    if 'math time' in voice_data:
        cpu_talk('Okay, math time!')
        math_data = record_audio('What is your problem?')
    if 'exit' in voice_data:
        cpu_talk('Okay, closing this program.  I hope you have a great rest of your day.')
        exit()
    
time.sleep(1)
print('Appp is now listening!')
while listen:
    voice_data = record_audio()
    respond(voice_data)
    

