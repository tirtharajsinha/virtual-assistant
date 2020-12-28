#################### library import ##################

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
from tkinter import *
from threading import Thread
import sys
import urllib.request
import re
import pandas as pd
import PIL
from PIL import Image,ImageTk
from tkinter import simpledialog
from tkinter import ttk

# library import part ends here
############################################
############# variable declaration #########
############################################
textheight=20
browserpath="C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(browserpath))
#########################################
########### SPEAKING ENGINE #############
#########################################

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)



def speak(audio):
    engine.setProperty("voice", voices[0].id)
    engine.setProperty('rate',170)
    engine.say(audio)
    engine.runAndWait()
def speakf(audio):
    engine.setProperty("voice", voices[1].id)
    engine.setProperty('rate',170)
    engine.say(audio)
    engine.runAndWait()

################################################
################# SUPPORTING FUNCTIONS #########
################################################

def newline(text):
    # align builder for text
    # any text before printing on gui canvas passes from here
    final=""
    for i in range(len(text)):
        final+=text[i]
        if i%20==0 and i!=0:
            final+="\n"

    return final
def write(text):
    # write test on canvas on gui
    global textheight
    canvas2.create_text(70, textheight, anchor=NW, text=newline(text), font="Helvetica 10 bold", fill="white")
    textheight += 40


def wishme():
    # starter function
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning tirtho")
    elif hour>12 and hour<18:
        speak("good afternoon tirtho!!")
    else:
        speak("good Evening tirtho")
    speak("This is leeo,Your personal helping hand,   how may i help you ?")

###################################################################
##################### SPEAK RECOGNITION fucntion ##################
###################################################################

def takecommand():
    global textheight
    #it will take mic input from user and return command as string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        canvas2.create_text(70,textheight,anchor=NW,text="Listening.....",font="Helvetica 15 bold", fill="white")
        textheight+=40
        r.pause_threshold=1
        r.energy_threshold = 200
        audio=r.listen(source)
    try:
        print("Recognising....")


        query=r.recognize_google(audio,language="en-in")
        print(f"You said..... {query}\n")

        canvas2.create_text(350, textheight, anchor=NW, text=newline(query), font="Helvetica 15 bold", fill="white")
        textheight += 40


    except Exception as e:
        # print(e)
        print("please,say that again.......")
        canvas2.create_text(70, textheight, anchor=NW, text="please,say that again.......", font="Helvetica 15 bold", fill="green")
        textheight += 40

        return "NONE"
    return query

#main conditional part starts here
####################################################|
############### MAIN APPLICATION ###################|
####################################################|

def startleo():
    global textheight
    wishlist = ["hi", "hello", "good morning", "good evening", "good night", "hey"]

    if __name__ == "__main__":
        wishme()
        while (True):
            query = takecommand().lower()
            query = query.replace("leo", "")
            wishele = [ele for ele in wishlist if (ele in query)]
            if wishele:
                speak("hello tirtho, nice to meet you.")

            if "thank" in query:
                speak("Welcome tirtho, your satisfaction is my perfection")
            elif "are you ok" in query or "how are you" in query:
                speak("absolutely fine,  remember me for any need,  i'm always here for you")
            elif "by" in query or "stop" in query or "goodbye" in query or "buy" in query or "bye" in query:
                speak("goodbuy,   see you later")
                break



            if "who am i" in query or "know me" in query:
                speak(
                    "you are   tirthoraj sinha  , softwre developer ,web developer, multilanguage programmer and  creator of me.")
            elif "who are you" in query or "who is you" in query or "who you" in query or "your name" in query:
                speak(
                    "hi, This is leeo  ,Tirtho's personal assistent,    built by tirtharaj,   always here for your need")
            elif "can do" in query or "you do" in query or "your work" in query:
                speak(
                    "i help tirtho in his work,    i find answer of your any relevent question and reply according to your query.")
                speak("ask anything")
            elif "time" in query or "date" in query:
                t = datetime.datetime.now().strftime("%H:%M:%S")
                ti = "it is " + t
                d = time.asctime(time.localtime(time.time())).split()
                date = " and date is " + d[0] + " " + d[1] + " " + d[2]
                current = ti + date
                print(current)
                canvas2.create_text(70, textheight, anchor=NW, text=newline(current), font="Helvetica 15 bold", fill="white")
                textheight += 40
                speak(current)
            elif " my brother" in query:
                speak(
                    "i never met your brother,jyotisko but he is well known for his foolishness,uselessness,   i also know he is called as hen")
            elif "repeat" in query:
                query=query.replace("repeat","")
                query=query.replace("me","")
                speak(query)
            elif "search" in query or "find" in query or "solve" in query or "what" in query or "who" in query:

                query = query.replace("tell", "")
                query = query.replace("search", "")
                query = query.replace("find", "")
                query = query.replace("wikipedia", "")
                f = open("apis.txt", "r")
                api = f.readlines()
                app_id = api[4].split(":")[1].strip()
                f.close()
                speak("searching......")

                if query.strip() == "":
                    speak("no query found,speak again")
                    continue

                if "google" in query:
                    query = query.replace("google", "")
                    webbrowser.get("chrome").open("https://www.google.com/search?q=" + query)
                    continue

                try:
                    client = wolframalpha.Client(app_id)
                    res = client.query(query)
                    result = next(res.results).text
                    speak("got it")
                    print(query, "\n", result)
                    canvas2.create_text(70, textheight, anchor=NW, text=newline(result), font="Helvetica 15 bold", fill="white")
                    textheight += 200
                    speak("according to web search      ")
                    speak(result)
                except Exception:
                    try:
                        result = wiki.summary(query, sentences=2)
                        print(query, "\n", result)
                        canvas2.create_text(70, textheight, anchor=NW, text=newline(result), font="Helvetica 15 bold",fill="white")
                        textheight += 200
                        speak("according to wikipedia  ")
                        speak(result)
                        pass
                    except:
                        speak("I have not understand, please say again")
                        continue



            elif "open" in query and "youtube" in query:
                speak("opening youtube....")
                print("opening youtube.....")
                canvas2.create_text(70, textheight, anchor=NW, text="opening youtube.....", font="Helvetica 15 bold",
                                    fill="white")
                textheight += 40
                try:
                    webbrowser.get("chrome").open("youtube.com")
                except Exception as e:
                    webbrowser.open("youtube.com")
                button.wait_variable(var)
            elif "open" in query and "google" in query:
                speak("opening google....")
                print("opening google.....")
                canvas2.create_text(70, textheight, anchor=NW, text="opening google.....", font="Helvetica 15 bold", fill="white")
                textheight += 40
                try:

                    webbrowser.get("chrome").open("google.com")

                except Exception as e:
                    webbrowser.open("google.com")
                # permission = input("press enter button to continue")
                button.wait_variable(var)
            elif "open" in query and "github" in query:
                speak("opening github....")
                print("opening github.....")
                canvas2.create_text(70, textheight, anchor=NW, text="opening github.....", font="Helvetica 15 bold",
                                    fill="white")
                textheight += 40
                try:
                    webbrowser.get("chrome").open("github.com")
                except Exception as e:
                    webbrowser.open("github.com")
                button.wait_variable(var)
            elif "open" in query and "instagram" in query:
                speak("opening instagram....")
                print("opening instagram.....")
                canvas2.create_text(70, textheight, anchor=NW, text="opening instagram.....", font="Helvetica 15 bold",
                                    fill="white")
                textheight += 40
                try:
                    webbrowser.get("chrome").open("instagram.com")
                except Exception as e:
                    webbrowser.open("instagram.com")
                button.wait_variable(var)
            elif ("personal" in query or "portfolio" in query or "my" in query) and "site" in query:
                speak("opening Tirtharaj Sinha official.........")
                try:
                    webbrowser.get("chrome").open("https://tirtharajsinha.github.io/webfiles/portfolio_v2.0")
                except Exception as e:
                    webbrowser.open("https://tirtharajsinha.github.io/webfiles/portfolio_v2.0")
                permission = input("press enter button to continue")
            elif "play" in query and("music" in query or "song" in query) and "youtube" not in query:
                music_dir = "F:\\direc\\chatbot music"
                songs = os.listdir(music_dir)
                music_ind = random.randint(0, len(songs) - 1)
                speak("sure tirtho,  playing music...." + songs[music_ind][:-4])
                os.startfile(os.path.join(music_dir, songs[music_ind]))

                button.wait_variable(var)
            elif "codeblock" in query or "c compiler" in query or "blocks" in query:
                apppath = "C:\Program Files (x86)\CodeBlocks\codeblocks.exe"
                os.startfile(apppath)
                speak("sure sir,    launching codeblocks....")
                button.wait_variable(var)
            elif "visual studio code" in query or "code" in query:
                apppath = "C:\\Users\\PINTU SINHA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(apppath)
                speak("sure sir,    launching visual studio code....")
                button.wait_variable(var)
            elif "pycharm" in query or "python" in query:
                apppath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
                os.startfile(apppath)
                speak("sure sir,    launching pycharm....")
                button.wait_variable(var)
            elif "atom" in query:
                apppath = "C:\\Users\\PINTU SINHA\\AppData\\Local\\atom\\atom.exe"
                os.startfile(apppath)
                speak("sure sir,    launching atom text editor....")
                button.wait_variable(var)
            elif "send" in query and "mail" in query:
                speak("mail wizerd is on")

                f = open("apis.txt", "r")
                api = f.readlines()
                sender = api[1].split(":")[1]
                passward = api[2].split(":")[1]
                f.close()
                speak("Enter the mail whom you want to send mail")
                canvas2.create_text(70, textheight, anchor=NW, text="Enter the mail whom you want to \nsend mail below text box",
                                    font="Helvetica 15 bold", fill="white")
                button.wait_variable(var)
                reciver = emailentry.get()

                if validate_email(reciver):
                    speak("email address verification done....")
                else:
                    speak("your email address is not valid")
                    print(reciver + " : is not a valid email address")
                    canvas2.create_text(70, textheight, anchor=NW, text=reciver + " : is not a valid email address",
                                        font="Helvetica 15 bold", fill="white")
                    textheight += 40

                speak("what will be your subject ?")
                esub = takecommand()
                sub = "Subject:" + esub + "\n"
                speak("what shold i write in body?")
                body = takecommand()
                if body == "NONE":
                    body = takecommand()
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
                joke = pyjokes.get_joke()
                print(joke)
                canvas2.create_text(70, textheight, anchor=NW, text=joke, font="Helvetica 15 bold",
                                    fill="white")
                textheight += 40
                speak(joke)
                speak("do you like the joke ?")
                feed = takecommand()
                if feed == "yes":
                    speak("my pleasure")
                else:
                    speak("i will try better next time")
            elif "weather" in query or "temperature" in query:

                if True:
                    f = open("apis.txt", "r")
                    api = f.readlines()
                    app_id = api[4].split(":")[1].strip()
                    f.close()
                    speak("fetching data......")

                    try:
                        client = wolframalpha.Client(app_id)
                        res = client.query(query)
                        result = next(res.results).text
                        speak("got it")
                        speak("according to web search  :" + result)
                        print(result)
                        canvas2.create_text(70, textheight, anchor=NW, text=result,
                                            font="Helvetica 15 bold", fill="white")
                        textheight += 40
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
                        if data["cod"] == 200:
                            speak("city found")
                            temp = data["main"]["temp"]
                            hum = data["main"]["humidity"]
                            visi = data["visibility"]
                            des = data["weather"][0]["description"]
                            main = "temparature is {} degree celcious , humidity is {} percent , visibitily is {} ,overall {}".format(
                                temp, hum, visi, des)
                            print("weather : " + main)
                            speak(main)
                            canvas2.create_text(70, textheight, anchor=NW, text=main,
                                                font="Helvetica 15 bold", fill="white")
                            textheight += 40
                        else:
                            speak("looks like some thing went wrong,city not found,try again")
            elif "my" in query and "location" in query:
                try:
                    res = requests.get("https://ipinfo.io/")
                    data = res.json()
                    ans = "city :" + data["city"] + ", country : " + data["country"] + ", region : " + data[
                        "region"] + " and time zone :" + data["timezone"]
                except:
                    ans = "sorry ! may be something wrong has been happend,try again ."

                print(ans)
                canvas2.create_text(70, textheight, anchor=NW, text=ans, font="Helvetica 15 bold",
                                    fill="white")
                textheight += 40
                speak(ans)
            elif ("project " in query) and ("folder" in query or "directory" in query or "file" in query):

                df = pd.read_csv("prj_path.csv")

                prlist = df["name"].tolist()
                mypath = ""

                for i in range(len(prlist)):
                    if prlist[i] in query:
                        mypath = df.iloc[i]["path"]
                        print("sure tirtho,  opening " + prlist[i] + " project directory")
                        speak("sure tirtho,  opening " + prlist[i] + " project directory")
                        canvas2.create_text(70, textheight, anchor=NW, text=newline("opening " + prlist[i] + " project directory"), font="Helvetica 15 bold",
                                            fill="white")
                        textheight += 40

                        break
                if mypath == "":
                    speak("which project will you like to open ?")
                    pathquery = takecommand()
                    if "project name" in pathquery or "which" in pathquery or "forgot" in pathquery:
                        prjstr=", ".join(prlist)
                        speak("you have not remembered your own projects, ha ha ha")
                        speak("jokes apart, your projects are"+prjstr)
                        write(prjstr)
                        speak("which project do you want to open?")
                        pathquery=takecommand()

                    for i in range(len(prlist)):
                        if prlist[i] in pathquery:
                            mypath = df.iloc[i]["path"]
                            print("sure tirtho,  opening " + prlist[i] + " project directory")
                            speak("sure tirtho,  opening " + prlist[i] + " project directory")
                            canvas2.create_text(70, textheight, anchor=NW,
                                                text=newline("opening " + prlist[i] + " project directory"),
                                                font="Helvetica 15 bold",
                                                fill="white")
                            textheight += 40
                            break


                if mypath=="":
                    mypath = df.iloc[-1]["path"]
                try:
                    webbrowser.open(mypath + "//")
                except:
                    speak("i have not gotten any project name")
                    break
            elif ("shut" in query or "turn of" in query) and ("computer" in query or "system" in query):
                speak("are you sure, that you want to shutdown your system,please type your final decision.")

                canvas2.create_text(70, textheight, anchor=NW,
                                    text=newline("Do you want to shutdown your system[y/n] : "),
                                    font="Helvetica 15 bold",
                                    fill="white")
                textheight += 40
                button.wait_variable(var)
                shut = emailentry.get()
                if shut.strip().lower() == "y":
                    # speak("sorry,  can't shutdown system")
                    # speak("this feature is currently turned off as application is under development")
                    speak("closing all application")
                    speak("shutting down your system")
                    os.system("shutdown /s /t 1")
                    # os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    break
                else:
                    speak("discarding shutdown decision")
                    time.sleep(5)
            elif ("play" in query or "search" in query) and "youtube" in query:
                speak("which song you want to listen?")
                rawquery = takecommand()
                if "play" in rawquery:
                    rawquery = rawquery.split("play")[1]
                queryl = rawquery.lower().strip().split()
                getquery = "+".join(queryl)

                if getquery != "":
                    url = "https://www.youtube.com/results?search_query=" + getquery
                    html = urllib.request.urlopen(url)
                    videoids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                    firstresult = "https://www.youtube.com/watch?v=" + videoids[0]
                    webbrowser.open(firstresult)
                    canvas2.create_text(70, textheight, anchor=NW,
                                        text=newline("press button below to continue...."),
                                        font="Helvetica 15 bold",
                                        fill="white")
                    textheight += 40
                    button.wait_variable(var)
                else:
                    speak("I haven't got proper query , please try again.")
            elif ("read" in query or "tell" in query or "today" in query) and "new" in query:
                f = open("apis.txt", "r")
                api = f.readlines()
                app_id = api[5].split(":")[1].strip()
                url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=" + app_id
                r = requests.get(url)
                data = json.loads(r.content)
                news = data["articles"]
                speak("sure sir, reading todays fresh news.......")
                for i in range(10):
                    print()
                    newstxt="news"+ str(i + 1)+" : "+ news[i]["title"]
                    canvas2.create_text(70, textheight, anchor=NW,
                                        text=newline(newstxt),
                                        font="Helvetica 10 bold",
                                        fill="white")
                    textheight += 100
                    if (i + 1) % 2 == 0:
                        speakf(news[i]["title"])
                        if i != 9:
                            speakf("moving to next news.")
                    else:
                        speak(news[i]["title"])
                        if i != 9:
                            speak("moving to next news.")
                speak("that's it for now, hope you enjoyed")

#application build ends here

######################################################
################# application driver #################
######################################################
def start():
    startleo()
    canvas2.create_text(40, textheight, anchor=NW, text="............  Leo Stopped .............", font="Helvetica 15 bold",
                        fill="white")
    print("leo stopped")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||| GUI DESIGN PORTION ||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#gui design strts here


if __name__=="__main__":
    root=Tk()
    root.title("Leo - Personal assistant")
    root.geometry("1000x800")
    root.configure(background="white")
    f1=Frame(root,width=400,height=760,bg="green")
    f1.pack(side=LEFT)
    image = Image.open("leointerface.jpg")
    photo = ImageTk.PhotoImage(image)
    labimg1 = Label(f1,image=photo)
    labimg1.pack()
    frame=Frame(root,width=570,height=720)
    frame.pack(side=RIGHT)
    var = IntVar()
    emailentry = Entry(root, textvariable=StringVar(),bg="black",fg="white",font=('Verdana',15))
    emailentry.place(x=410,y=730,height=50,width=520)
    button = Button(root, text="Click Me", command=lambda: var.set(1))
    button.place(x=920,y=730,height=50,width=60)

    canvas2=Canvas(frame,bg="goldenrod2",width=570,height=720,scrollregion=(0,0,580,4000))
    vbar=Scrollbar(frame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas2.yview)
    canvas2.config(yscrollcommand=vbar.set)
    canvas2.pack(expand=True,fill=BOTH)
    task=Thread(target=start)
    task.start()
    root.mainloop()


