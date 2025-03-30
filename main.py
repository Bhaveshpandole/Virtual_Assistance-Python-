import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open groww" in c.lower():
        webbrowser.open("https://groww.in")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/Bhaveshpandole")
    elif "open translator" in c.lower():
        webbrowser.open("https://translate.google.co.in/?sl=auto&tl=en&op=translate")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 

if __name__ == "__main__":
    speak("Initializing laptop...")
    while True:
    #listen for the wake word jarvis
    # obtain audio from the microphone

        r = sr.Recognizer()
       

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if(word.lower() == "laptop"):       #voice command
                speak("Haa bol")                #return
                #listen for command
                with sr.Microphone() as source:
                    print("laptop Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))