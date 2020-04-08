import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
   
    '''
    This function is used for wishing the user according to system time. This introduces our bot as well.
    '''
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        print("Clib : Good Morning!",end=" ")
        speak("Good Morning! mister Yashpal Singh Shekhawat")
        
        
    elif hour>=12 and hour<18:
        print("Clib : Good Afternoon!",end=" ")
        speak("Good Afternoon!")
    else:
        print("Clib : Good Evening!",end=" ")
        speak("Good Evening!")
    print("I am Clib. ")
    speak("I am Clib.")
    print("Clib : I request you to answer using the keywords I use in the question, so I can help you better")
    
def takeCommand():
    
    '''
    It takes microphone input from the user and returns string output.
    '''
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en=in')
        print("User : " +query)
              
              
    except Exception as e:
              print(e)
              print("Say that again please...")
              return "None"
    
    return query
if __name__  == "__main__":
    wishMe()
    while 1:
        a=takeCommand()
        if a=="open Chrome":
            system.os('cd "\Program Files (x86)\Google\Chrome\Application"')
            system.os("chrome")
        if a=="open Visual Studio"or a=="open Visual Code":
            os.system("code")
        if "Time" in a or 'time'in a:
            now=datetime.datetime.now()
            speak("it's"+now.strftime("%H")+now.strftime("%M"))
        if 'date' in a or 'Date' in a:
            now=datetime.datetime.now()
            speak("today is "+str(int(now.strftime("%d")))+" "+now.strftime("%B")+now.strftime("%Y"))
        if 'this PC' in a:
            pass
        if 'google' in a or 'Google'in a:
            webbrowser.open_new_tab("www.google.com")
        if 'Youtube' in a or 'youtube' in a:
            webbrowser.open_new_tab("www.youtube.com")
        if 'WhatsApp' in a:
            webbrowser.open_new_tab("www.whatsapp.com")
        if 'song' in a or 'Song' in a:
            webbrowser.open_new_tab("www.gaana.com")
        if 'close' in a or 'Close' in a:
            break
        elif '':
            speak("related result not found")
