import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import subprocess as subP
import keyFunc as kf
from gtts import gTTS
from time import ctime
listen = True
r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            cpu_talk(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            # print(voice_data)
        except sr.UnknownValueError:
            print('',end='')
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

def respond(voice_data,passed=''):
    voice_data = voice_data.lower()
    if 'computer' in voice_data or len(passed) > 0:
        if 'what time is it' in voice_data or 'what time is it' in passed:
            fullStr = ctime().split()
            timeStr = fullStr[3]
            cpu_talk('1')
            cpu_talk('01')

        elif 'search Google' in voice_data or 'search Google' in passed:
            search = record_audio('What would you like to search Google for?')
            url = 'https://google.com/search?q='+search
            webbrowser.get().open(url)
            cpu_talk(f'Your Google search for {search} returned the following!')
        elif 'search Bing' in voice_data or passed and 'search Bing' in passed:
            search = record_audio('What would you like to search Bing for?')
            url = 'https://bing.com/search?q='+search
            webbrowser.get().open(url)
            cpu_talk(f'Your Google search for {search} returned the following!')
        # elif 'what\'s your name?' in voice_data:
        #     print('what!')
        elif 'location' in voice_data or passed and 'location' in passed:
            location = record_audio('Please provide a location?')
            url = 'https://google.com/maps/search/'+location
            webbrowser.get().open(url)
            cpu_talk(f"Here's what I found for {location} using Google Map Search!")
        elif 'site' in voice_data or passed and 'site' in passed:
            theUrl = record_audio('What site would you like to visit?')
            webbrowser.get().open('http://'+theUrl)
            cpu_talk('Here\'s '+theUrl)
        elif 'directions' in voice_data or passed and 'directions' in passed:
            from_data = record_audio('What is your starting point?')
            to_data = record_audio('What is your ending point?')
            webbrowser.get().open('https://google.com/maps/dir/'+from_data+'/'+to_data+'/')
        elif 'math' in voice_data or passed and 'math' in passed:
            cpu_talk('Okay, math time! Watch me shine!')
            mathStr = record_audio('What do you need help with?')
            theAnswer = someMath(mathStr)
            cpu_talk(f"The answer is {theAnswer}!")
        elif 'exit' in voice_data or passed and 'exit' in passed:
            cpu_talk('Okay, closing this program.  I hope you have a great rest of your day.')
            exit()
        else:
            if len(passed) > 0:
                cannotHear = record_audio('Sorry, I didn\'t understand, can you state your action again?')
                respond('',cannotHear)
            else:
                info = record_audio('How can I help you!')
                respond('',info)
def someMath(str):
    newStr = str.split()
    mathStr = ''
    for inf in newStr:
        try:
            int(inf)
            mathStr += inf
        except ValueError:
            if inf == '+' or inf == '-' or inf == '/' or inf == '*':
                mathStr += inf
    return eval(mathStr)

time.sleep(1)
print('App is now listening!')
while True:
    voice_data = record_audio()
    respond(voice_data)

