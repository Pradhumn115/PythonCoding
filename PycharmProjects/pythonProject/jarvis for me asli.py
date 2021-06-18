import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import CoreServices


engine = pyttsx3.init('nsss')

client = wolframalpha.Client('42JV6J-469TH7TH94')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[31].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('नमस्ते!')

    if currentH >= 12 and currentH < 18:
        speak('जय श्री राम!')

    if currentH >= 18 and currentH !=0:
        speak('जय श्री कृष्णा!')

greetMe()

speak('हैलो सर, मैं आपका डिजिटल सहायक जार्विस हूं')
speak('मैं आपकी मदद कैसे कर सकता हूं?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.energy_threshold = 500
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('क्षमा करें श्रीमान! मुझे नहीं समझ आया! कमांड टाइप करने की कोशिश करें!')
        query = (str(input('Command: ')))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()

        if 'youtube' in query:
            new=2 
            url="http://youtube.com"
            webbrowser.open(url,new=new)

        elif 'google' in query:
            new=2 
            url="http://google.com"
            webbrowser.open(url,new=new)

        elif 'stackoverflow' in query:
            new=2 
            url="http://stackoverflow.com"
            webbrowser.open(url,new=new)

        elif 'gmail' in query:
            new=2
            url="http://gmail.com"
            webbrowser.open(url,new=new)

            # music or gana list from internet:

        elif 'gano ki list' in query or 'gane ki list' in query:
            speak('गाने की लिस्ट इस प्रकार है')
            gane = ("'bala',\ 'coca cola tu',\ 'kaun hai voh(bahubali)',\ 'mahishmati samrajya',\ 'jiyo re baahubali',\ 'jay jay kara'")
            m = ("'बाला', \ 'कोका कोला तू', \ 'कौन है वो (बाहुबली)', \ 'माहिष्मती साम्राज्य', \ 'जियो रे बाहुबली', \ _ 'जय जय कार'")
            print(gane)
            speak(m)

        elif 'bala' in query:
            new=2
            url="https://www.youtube.com/watch?v=PHwPdwADXV0"
            webbrowser.open(url,new=new)
            speak('गाने का आनंद लें!')

        elif 'coca cola' in query or 'Coca-Cola' in query:
            new=2
            url="https://www.youtube.com/watch?v=_cPHiwPqbqo"
            webbrowser.open(url,new=new)
            speak('गाने का आनंद लें!')

        elif 'kaun hai voh' in query or 'kaun hai vah' in query or 'kaun hai woh' in query:
            new=2
            url="https://www.youtube.com/watch?v=WibcvWT7KQQ&list=PLMHdjxes1-5ki4rzsgzuIJqSZqBWLyjH7&index=1"
            webbrowser.open(url,new=new)
            speak('गाने का आनंद लें!')

        elif 'mahishmati Samrajya' in query or 'maheshmati samrajya' in query:
            new=2
            url="https://www.youtube.com/watch?v=aK9ohIzeYSk&list=PLMHdjxes1-5ki4rzsgzuIJqSZqBWLyjH7&index=8"
            webbrowser.open(url,new=new)
            speak('गाने का आनंद लें!')

        elif 'jiyo re bahubali' in query or 'jio re bahubali' in query:
            new=2
            url="https://www.youtube.com/watch?v=k-atPa3QUis&list=PLMHdjxes1-5ki4rzsgzuIJqSZqBWLyjH7&index=5"
            webbrowser.open(url,new=new)
            speak('गाने का आनंद लें!')

        elif 'jay jay kara' in query or 'jai jai kara' in query:
            new=2
            url="https://www.youtube.com/watch?v=F-JoqgpSsBc"
            webbrowser.open(url,new=new)
            speak('गाने का आनंद लें!')

        elif 'avengers assemble' in query or 'avengers ki tune' in query:
            new=2
            url="https://www.youtube.com/watch?v=xmU1upyu_J8"
            webbrowser.open(url,new=new)
            speak('गाने का आनंद लें!')
        
        # जारविस khud bole nam
        elif 'tum' in query or 'tumhara nam' in query:
            speak("में आपका डिजिटल सहायक हूँ और आपका पर्सनल असिस्टेंट")
        

        
        elif 'game' in query:
            new=2
            url="https://tankionline.com"
            webbrowser.open(url,new=new)

        elif 'padhai' in query:
            new=2
            url="https://www.learncbse.in"
            webbrowser.open(url,new=new)

        elif 'test' in query:
            new=2
            url="https://mycbseguide.com/course/cbse-class-09/1217/"
            webbrowser.open(url,new=new)
        elif 'paper' in query:
            new=2
            url="https://www.vedantu.com/home"
            webbrowser.open(url,new=new)

        
        elif 'time' in query or 'samay' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, समय है {strTime }")



        elif "kya chal raha hai" in query or 'kese ho' in query or 'kaise ho' in query:
            stMsgs = ['बस कुछ काम कर रहा था!', 'मै खुश हू!', 'थीक हू!', 'मसे मे हू!']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('पाने वाला कौन है? ')
            recipient = myCommand()

        


            if 'Khud' in recipient:
                try:
                    speak('मैं क्या कहूँ ? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("pradhumn.115@gmail.com", 'manugupta')
                    server.sendmail('pradhumn.115@gmail.com', "pradhumn.115@gmail.com", content)
                    server.close()
                    speak('Email sent!')

            


                except:
                    speak('क्षमा करें श्रीमान! मैं इस समय आपका संदेश भेजने में असमर्थ हूँ!')


        elif 'kuch nahi' in query or 'band' in query or 'ruko' in query:
            speak('okay')
            speak('Bye Sir, आपका दिन शुभ हो')
            sys.exit()
           
        elif 'hello' in query or 'hi' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, आपका दिन शुभ हो')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = 'https://www.youtube.com/watch?v=wplnSnIBOYc&list=PL4uUU2x5ZgR1JOlcY9SZB94MW6fBE8ovU'
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  

            speak('Okay, here is your music! Enjoy!')
            

        else:
            query = query
            speak('खोज रहा हूँ..')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('मिल गया.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('मिल गया.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('और क्या कर सकता हूँ')
