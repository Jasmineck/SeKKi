import pyttsx3
import speech_recognition as recognize
import datetime #inbuilt
import wikipedia
import webbrowser #inbuilt
import os #inbuilt
import random
import pyautogui #programitically controls mouse and keyboard
import numpy as np
import cv2 # also need to install pip install Pillow --upgrade  #for screenshot



engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.setProperty("rate", 178)
    engine.runAndWait()

def greetings():
    print("Sekkei  ACT 1 Loading....")
    speak("Sekkei,  ACT 1,. Loading!....")
    print(" Installing Data.........")
    speak(" Installing data!.........")
    speak(".......")
    print(" Preparation Complete!")
    speak(" preparation complete!.")
    speak(" Launching A I ")

    hrs = datetime.datetime.now().hour #returns current time in 24-hrs format
    
    if hrs>=0 and hrs<12:
        speak("Good Morning Mistress")
    elif hrs>=12 and hrs<16:
        speak("Good Afternoon Mistress")
    else:
        speak("Good Evening Mistress")
    
def commands():
    #takes voice input and convert it into string
    
    r= recognize.Recognizer()
    with recognize.Microphone() as source:
        print("Processing...")
        r.pause_threshold =1 #seconds after which program stops recording audio
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        speak("sekkei is not able to get you mistress, Please!say that again?")
        return "None"
    return query

if __name__ == "__main__":
    greetings()
    while True:
        query=commands().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query=query.replace("wikipedia","")
            result= wikipedia.summary(query, sentences=2)
            speak( "A ccording to wikipedia....")
            print(result)
            speak(result)
        elif 'launch youtube' in query:
            webbrowser.open('youtube.com')
        elif 'launch google' in query:
            webbrowser.open('google.com')
        elif 'launch codechef' in query:
            webbrowser.open('codechef.com')
        elif 'launch' in query:
            speak('please tell me the name of website to be launched')
            query=query.replace('launch','')
            web='https://www,'+ query + '.com'
            webbrowser.open(web)
            speak('is this what u asked for Mistress?')

        
        #-------------------------------------------------------------------------------------------------
        elif 'search' in query:
            if 'google' in query:
                speak('ok mistress,This is what i found on Google')
                query=query.replace('google','')
                query=query.replace('search','')
                query=query.replace('on','')
                web='https://www.google.com/search?q=='+query
                webbrowser.open(web)
            elif 'youtube' in query:
                speak('ok mistress,This is what i found on You Tube')
                query=query.replace('youtube','')
                query=query.replace('search','')
                query=query.replace('on','')
                web='https://www.youtube.com/results?search_query='+query
                webbrowser.open(web)
            else :continue
        #----------------------------------------------------------------------------------------------------
        elif 'song' in query:
            musix='D:\\my musix' #location of song file in the operating system
            songs=os.listdir(musix)  #listdir,startfile etc. are all functions of os module
            print(songs)
            a=random.randint(0,6)
            speak("hope you like this song mistress?")
            os.startfile(os.path.join(musix,songs[a]))
        elif 'code' in query:
            vs_code="C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('Launching V S code')
            os.startfile(vs_code)
        elif 'blender' in query:
            blender="C:\\Program Files\\Blender Foundation\\Blender 2.92\\blender.exe"
            speak('Launching 3 D blender')
            os.startfile(blender)
        elif 'minecraft' in query:
            minecraft="C:\\Users\\Hp\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            speak("Launching Minecraft")
            os.startfile(minecraft)
        elif 'impact' in query:
            genshin="C:\\Program Files\\Genshin Impact\\launcher.exe"
            speak("Launching Genshim Impact")
            os.startfile(genshin)
        elif 'discord' in query:
            discord='C:\\Users\\Hp\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe'
            speak("Lunching Discord")
            os.startfile(discord)
        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
            cv2.imwrite("image1.png", image)

            





        elif 'time' in query:
            tym=datetime.datetime.now().strftime("%H:%M:%S:")  #STARFTIME CONVERTS DATE AND TIME TO STRING
            day=datetime.datetime.today().strftime("%A") #datime rfeturns integer value so to get exact day we need to convert it into strings
            speak("Today is")
            speak(day)
            speak("and the TIME is,")
            speak(tym)



    