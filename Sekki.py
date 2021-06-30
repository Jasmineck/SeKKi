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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #provide access to keyboard keys
import time

engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.setProperty("rate", 178)
    engine.runAndWait()

def greetings():
    print("Sekkei  ACT 1 Loading....")
    speak("Sekkei,  ACT 1,. Loading!....")
    print("Installing Data.........")
    speak("Installing data!.........")
    speak(".......")
    print("Preparation Complete!")
    speak("preparation complete!.")
    speak("Launching A I ")

    hrs = datetime.datetime.now().hour #returns current time in 24-hrs format
    
    if hrs>=0 and hrs<12:
        speak("Good Morning Mistress")
    elif hrs>=12 and hrs<16:
        speak("Good Afternoon Mistress")
    else:
        speak("Good Evening Mistress")
    time.sleep(2)
    speak("How may i help you mistress?")
    
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
        
        if 'launch youtube' in query:
            webbrowser.open('youtube.com')
        elif 'launch google' in query:
            webbrowser.open('google.com')
        elif 'launch codechef' in query:
            webbrowser.open('codechef.com')
        #elif 'launch' in query:
            #speak('please tell me the name of website to be launched')
            #query=query.replace('launch','')
            #web='https://www,'+ query + '.com'
            #webbrowser.open(web)
            #speak('is this what u asked for Mistress?')

        
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
            elif 'wikipedia' in query:
                speak("Searching wikipedia.....")
                query=query.replace("wikipedia","")
                result= wikipedia.summary(query, sentences=2)
                speak( "A ccording to wikipedia....")
                print(result)
                speak(result)
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
            speak('the screenshot is taken mistress')
            time.sleep(2)

            





        elif 'time' in query:
            tym=datetime.datetime.now().strftime("%H:%M:%S:")  #STARFTIME CONVERTS DATE AND TIME TO STRING
            day=datetime.datetime.today().strftime("%A") #datime rfeturns integer value so to get exact day we need to convert it into strings
            speak("Today is")
            speak(day)
            speak("and the TIME is,")
            speak(tym)

        

        #----------------------------------------------------------------------------------------------------------------------------------------------------
        
        #SELENIUN
        
        elif 'assignment' in query:
            driver = webdriver.Chrome(executable_path="D:\\VS F\\Python\\Sekki\\drivers\\chromedriver.exe")
            driver.get("https://edu.google.com/intl/en_in/products/classroom/?gclid=CjwKCAjw2ZaGBhBoEiwA8pfP_jaN4keRSzKCLk9grHBMXJkpu9TvuiXVQspHpvE5BTjktbMLEcdj2BoCankQAvD_BwE&gclsrc=aw.dsADBUDIIIP-O89'P[")
            driver.find_element_by_xpath('//*[@id="gfe-main-content"]/section[1]/div/div/div/ul/li[2]/a/span').click()
            time.sleep(10)

            
            
        #-----------------------------------------------------------------------------------------------------------------------------------------------------    
        
        #To-Do List [SELENIUM]

        elif 'to do' in query:
            driver = webdriver.Chrome(executable_path="D:\\VS F\\Python\\Sekki\\drivers\\chromedriver.exe")
            driver.get("https://redocamai.github.io/To-do-List/")
            title=driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/div[1]/input')
            speak('Add title for task Mistress!')
            title_input=commands()
            title.send_keys(title_input)
            descp=driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/textarea')
            speak('Add Discription for the task Mistress!')
            descp_input=commands()
            descp.send_keys(descp_input)
            speak('plese select the due date mistress')
            time.sleep(15)
            speak('Are you done Mistress? should i add this to the list')
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div/div[1]/button').click()
            speak(title_input)
            speak('added to To Do list')
            






        


        #----------------------------------------------------------------------------------------------------------------------------------------------------
        
        #GAMES
        elif 'game' in query:
            speak('Which Game do u want to play mistress?')
            print('1. Rock ,Paper, sissor \n',"2.")
            
            #speak('say 1 for Rock,Paper,Sissor')



        #ROCK / PAPER / SISSOR
            speak('...')
            speak(' Rock, Paper, Sissor game loading....')
            speak('Say your choice mistress')
            speak(' Rock, Paper OR Sissor')
            choices=['rock','paper','sissor']
            comp=random.choice(choices)
            while True:
                print('Listining.....')
                user=commands().lower()
                if user=='stop':
                    speak('Thanks for playing with me mistress')
                    break
                if user=='rock':
                    user='rock'
                elif user=='paper':
                    user= 'paper'
                else:
                    user='sissor'   #since sekki can't detect certin words properly we had to use if else to assign valid values
                
                print('User choose : ',user)
                speak('user choosed :')
                speak(user)

                print('seKKi choose : ',comp)
                speak('I choose :')
                speak(comp)

                if comp==user:
                    print('DRAW!')
                    speak('The match is draw!')
                elif user=='rock':
                    if comp== 'paper':
                        print('YOU LOSE!!')
                        speak('Sorry mistress you lost this round')
                    else:
                        print('YOU WIN!!!')
                        speak('Congrats mistress... YOU WON!')
                elif user=='paper':
                    if comp== 'sissor':
                        print('YOU LOSE!!')
                        speak('Sorry mistress you lost this round')
                    else:
                        print('YOU WIN!!!')
                        speak('Congrats mistress... YOU WON!')
                else:
                    
                    if comp== 'rock':
                        print('YOU LOSE!!')
                        speak('Sorry mistress you lost this round')
                    else:
                        print('YOU WIN!!!')
                        speak('Congrats mistress... YOU WON!')


            


            
        #-----------------------------------------------------------------------------------------------------------------------------------------------------


        #CALCULATOR


        elif 'calculate' in query:


            print("Say the number to be calculated \n","eg: \n","6 Plus 5 \n","7 Minus 9 \n", "5 Multiplied by 3 \n","8 Divided by 4 \n")
            print("say 'Stop' to exit")
            speak('Say the number to be calculated')
            speak("FOR EXAMPLE : 6 Plus 5")
            sum=0

            while True:
                print("say the numbers........")
                
                calc=commands().lower()
                x=[]
                x=calc.split() # we are dividing the voice input into 3 parts...2 oprands and a operator
                print(x)
                if calc == "stop":
                    break
                else:
                    if x[1]=='+':
                        x[0]=int(x[0])
                        x[2]=int(x[2])
                        y=x[0]+x[2]
                        sum=y
                        print("Answer :",y)
                        speak(" the answer is")
                        speak(y)
                    elif x[1]== 'x' :
                        x[0]=int(x[0])
                        x[2]=int(x[2])
                        y=x[0] * x[2]
                        sum=y
                        print("Answer :",y)
                        speak(" the answer is")
                        speak(y)
                    elif x[1]=='/':
                        x[0]=int(x[0])
                        x[2]=int(x[2])
                        y=x[0]/[2]
                        sum=y
                        print("Answer :",y)
                        speak(" the answer is")
                        speak(y)
                    elif x[1]=='-':
                        x[0]=int(x[0])
                        x[2]=int(x[2])
                        y=x[0]-x[2]
                        sum=y
                        print("Answer :",y)
                        speak(" the answer is")
                        speak(y)
                    else:
                        speak("Sorry Mistress i didn't get it please try again!")
                
    #-----------------------------------------------------------------------------------------------------------------------------------
            
        elif 'stop' in query:
            break           


    #-------------------------------------------------------------------------------------------------------------------------------------
        elif 'introduce' in query:
            speak('Hello everyone! I am Sekkei. I am a personalised voice operated Desktop assistant')
            speak(" Sekkei can interpret human speech and respond via synthesized voices")
            speak("I can perform tasks based on my mistress's commands.")
            speak("you can ask Sekkei questions, control home automation devices,play games and media playback via voice, and manage other basic tasks such as email, to-do lists, and calendars with verbal commands")
            speak("To know Sekkei in a better way you can ask for Help in commands. Also do check out Sekki's source code on Git Hub to understand how i work")
            webbrowser.open('https://github.com/Jasmineck/SeKKi')
            speak('This Kawaei git Hub page is my home UwU')
           
            speak('Hope you like spending tyme with sekkei. Aahhh Kemochee!')
            speak('My mistress is GOD!')

   #---------------------------------------------------------------------------------------------------------------------------------------

        elif 'help' in query:
            speak("Here are Sekkei's Basic commands")
            webbrowser.open("https://github.com/Jasmineck/SeKKi#how-to-use-sekki-")
            time.sleep(15)

    #---------------------------------------------------------------------------------------------------------------------------------------