#this is leo, vertual assistant - built by Tirtharaj Sinha @tirtharajsinha

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import time
import webbrowser
import os
import random
import smtplib
from validate_email import validate_email
import pyjokes
import requests
import json
import wolframalpha
# library import part ends here

# variable declear part starts here

browserpath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(browserpath))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)



def speak(audio):
    engine.setProperty('rate',170)
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning tirtho")
    elif hour>12 and hour<18:
        speak("good afternoon tirtho!!")
    else:
        speak("good Evening tirtho")
    speak("This is leeo,Your personal helping hand,   how may i help you ?")

def takecommand():
    #it will take mic input from user and return command as string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshold = 200
        audio=r.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio,language="en-in")
        print(f"You said..... {query}\n")
    except Exception as e:
        # print(e)
        print("please,say that again.......")
        return "NONE"
    return query

#main conditional part starts here

wishlist=["hi","hello","good morning","good evening","good night","hey"]

if __name__=="__main__":
    wishme()
    while(True):
        query=takecommand().lower()
        query=query.replace("leo","")
        wishele=[ele for ele in wishlist if(ele in query)]
        if wishele:

            speak("hello tirtho, nice to meet you.")


        if "thank" in query:
            speak("Welcome tirtho, your satisfaction is my perfection")
        elif "are you ok" in query or "how are you" in query:
            speak("absolutely fine,  remember me for any need,  i'm always here for you")
        elif "by" in query or "stop" in query or "goodbye" in query or "buy" in query or "bye" in query:
            speak("goodbuy,   see you later")
            break
        elif "who am i" in query or "know me" in query:
            speak("you are   tirthoraj sinha  , softwre developer ,web developer, multilanguage programmer and  creator of me.")
        if "who are you" in query or "who is you" in query or "who you" in query or "your name" in query:
            speak("hi, This is leeo  ,Tirtho's personal assistent,    built by tirtharaj,   always here for your need")
        if  "can do" in query or "you do" in query or "your work" in query:
            speak("i help tirtho in his work,    i find answer of your any relevent question and reply according to your query.")
            speak("ask anything")
        if "time" in query or "date" in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            ti = "it is " + t
            d = time.asctime(time.localtime(time.time())).split()
            date = " and date is " + d[0] + " " + d[1] + " " + d[2]
            current = ti + date
            print(current)
            speak(current)
        if " my brother" in query:
            speak("i never met your brother,jyotisko but he is well known for his foolishness,uselessness,   i also know he is called as hen")


        if "search" in query or "find" in query or "solve" in query:

            query=query.replace("tell","")
            query = query.replace("search", "")
            query = query.replace("find", "")
            query = query.replace("wikipedia", "")
            f = open("apis.txt", "r")
            api = f.readlines()
            app_id = api[4].split(":")[1].strip()
            f.close()
            speak("searching......")
            if query.strip()=="":
                speak("no query found,speak again")
                continue

            try:
                client = wolframalpha.Client(app_id)
                res = client.query(query)
                result=next(res.results).text
                speak("got it")
                print(query, "\n", result)
                speak("according to web search      ")
                speak(result)
            except Exception:
                try:
                    result = wiki.summary(query, sentences=2)
                    print(query, "\n", result)
                    speak("according to wikipedia      ")
                    speak(result)
                    pass
                except:
                    speak("I have not understand, please say again")
                    continue



        elif "open" in query and "youtube" in query:
            speak("opening youtube....")
            print("opening youtube.....")
            try:
                webbrowser.get("chrome").open("youtube.com")
            except Exception as e:
                webbrowser.open("youtube.com")
            permission=input("press enter button to continue")
        elif "open" in query and "google" in query:
            speak("opening google....")
            print("opening google.....")
            try:
                webbrowser.get("chrome").open("google.com")
            except Exception as e:
                webbrowser.open("google.com")
            permission = input("press enter button to continue")
        elif "open" in query and "github" in query:
            speak("opening github....")
            print("opening github.....")
            try:
                webbrowser.get("chrome").open("github.com")
            except Exception as e:
                webbrowser.open("github.com")
            permission=input("press enter button to continue")
        elif "open" in query and "instagram" in query:
            speak("opening instagram....")
            print("opening instagram.....")
            try:
                webbrowser.get("chrome").open("instagram.com")
            except Exception as e:
                webbrowser.open("instagram.com")
            permission=input("press enter button to continue")
        elif "play" in query and("music" in query or "song" in query):
            music_dir="F:\\direc\\chatbot music"
            songs=os.listdir(music_dir)
            music_ind=random.randint(0,len(songs)-1)
            speak("sure tirtho,  playing music...." + songs[music_ind][:-4])
            os.startfile(os.path.join(music_dir,songs[music_ind]))

            permission = input("press enter button to continue")
        elif "codeblock" in query or "c compiler" in query or "blocks" in query:
            apppath="C:\Program Files (x86)\CodeBlocks\codeblocks.exe"
            os.startfile(apppath)
            speak("sure sir,    launching codeblocks....")
            permission = input("press enter button to continue")
        elif "visual studio code" in query or "code" in query:
            apppath="C:\\Users\\PINTU SINHA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(apppath)
            speak("sure sir,    launching visual studio code....")
            permission = input("press enter button to continue")
        elif "pycharm" in query or "python" in query:
            apppath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(apppath)
            speak("sure sir,    launching pycharm....")
            permission = input("press enter button to continue")
        elif "atom" in query:
            apppath="C:\\Users\\PINTU SINHA\\AppData\\Local\\atom\\atom.exe"
            os.startfile(apppath)
            speak("sure sir,    launching atom text editor....")
            permission = input("press enter button to continue")
        elif "send" in query and "mail" in query:
            speak("mail wizerd is on")

            f = open("apis.txt", "r")
            api = f.readlines()
            sender = api[1].split(":")[1]
            passward = api[2].split(":")[1]
            f.close()
            speak("Enter the mail whom you want to send mail")
            reciver = input("enter reciver's mail id : ")
            if validate_email(reciver):
                speak("email address verification done....")
            else:
                speak("your email address is not valid")
                print(reciver + " : is not a valid email address")

            speak("what will be your subject ?")
            esub=takecommand()
            sub = "Subject:" + esub + "\n"
            speak("what shold i write in body?")
            body=takecommand()
            if body=="NONE":
                body=takecommand()
            message = sub + body

            try:

                smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpObj.starttls()
                smtpObj.login(sender, passward)
                try:
                    smtpObj.sendmail(sender, reciver, message)
                    speak("sucessfully mail sent")
                    smtpObj.quit()
                except Exception:
                    speak("looks like some problem has been occured")
                    smtpObj.quit()


            except Exception:
                speak("i could not able to login")
                smtpObj.quit()
        elif "tell" in query and "joke" in query:
            speak("sure tirtho      ")
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
            speak("do you like the joke ?")
            feed=takecommand()
            if feed=="yes":
                speak("my pleasure")
            else:
                speak("i will try better next time")
        elif "weather" in query:

            if True:
                f = open("apis.txt", "r")
                api = f.readlines()
                app_id = api[4].split(":")[1].strip()
                f.close()
                speak("searching......")

                try:
                    client = wolframalpha.Client(app_id)
                    res = client.query(query)
                    result = next(res.results).text
                    speak("got it")
                    speak("according to web search  :"+result)
                    print(result)
                except:
                    baseurl = "http://api.openweathermap.org/data/2.5/weather?q="
                    f = open("apis.txt", "r")
                    api = f.readlines()
                    weatherapi = api[3].split(":")[1].strip()
                    speak("please, name the place")
                    place = takecommand()
                    url = baseurl + place + "&appid=" + str(weatherapi) + "&units=metric"
                    res = requests.get(url)
                    data = res.json()
                    if data["cod"]==200:
                        speak("city found")
                        temp=data["main"]["temp"]
                        hum=data["main"]["humidity"]
                        visi=data["visibility"]
                        des=data["weather"][0]["description"]
                        main="temparature is {} degree celcious , humidity is {} percent , visibitily is {} ,overall {}".format(temp,hum,visi,des)
                        print("weather : "+main)
                        speak(main)
                    else:
                        speak("looks like some thing went wrong,city not found,try again")
        elif "my" in query and "location" in query:
            try:
                res = requests.get("https://ipinfo.io/")
                data = res.json()
                ans="city :"+data["city"]+", country : "+data["country"]+", region : "+data["region"] +" and time zone :"+data["timezone"]
            except:
                ans="sorry ! may be something wrong has been happend,try again ."

            print(ans)
            speak(ans)
        else:
            speak("i didn't get that, can you say again ?")












