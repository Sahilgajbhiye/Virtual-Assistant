import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from tkinter import *
from PIL import Image, ImageTk  # For handling background images

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        update_gui("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        update_gui("Good Afternoon!")
    else:
        speak("Good Evening!")
        update_gui("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you.")
    update_gui("I am Jarvis Sir. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        update_gui("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        update_gui("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        update_gui(f"User said: {query}")
        return query.lower()
    except Exception as e:
        update_gui("Say that again please...")
        return "none"

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        update_gui("Email has been sent!")
    except Exception as e:
        update_gui("Unable to send the email.")

def processCommand():
    query = takeCommand()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        update_gui(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        update_gui("Opening YouTube")

    elif 'open google' in query:
        webbrowser.open("google.com")
        update_gui("Opening Google")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
        update_gui("Opening Stack Overflow")

    elif 'play music' in query:
        webbrowser.open("https://open.spotify.com/track/2VQ4UC9dNVPDLge8lr9USm")
        update_gui("Playing music")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        update_gui(f"Sir, the time is {strTime}")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        update_gui("Opening Visual Studio Code")

    elif 'email to harry' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "harryyourEmail@gmail.com"
            sendEmail(to, content)
        except Exception as e:
            speak("Sorry, I am not able to send this email.")
            update_gui("Failed to send email.")

# GUI Functions
def update_gui(text):
    text_area.config(state=NORMAL)
    text_area.insert(END, text + "\n")
    text_area.config(state=DISABLED)
    text_area.yview(END)

def start_jarvis():
    wishMe()
    processCommand()

# GUI Setup
root = Tk()
root.title("Jarvis Virtual Assistant")
root.geometry("600x700")

# Adding Background Image
bg_image = Image.open("voice.jpg")  
bg_image = bg_image.resize((300,500), Image.ANTIALIAS)  # Resize to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Set the image as the background

# Adding GUI Elements
label = Label(root, text="Jarvis - Virtual Assistant", font=("Helvetica", 18, "bold"), bg="black", fg="white")
label.pack(pady=10)

text_area = Text(root, wrap=WORD, font=("Helvetica", 12), state=DISABLED, bg="white", fg="black")
text_area.pack(pady=10, fill=BOTH, expand=True)

start_button = Button(root, text="Start Jarvis", command=start_jarvis, font=("Helvetica", 14), bg="green", fg="white")
start_button.pack(pady=20)

exit_button = Button(root, text="Exit", command=root.quit, font=("Helvetica", 14), bg="red", fg="white")
exit_button.pack(pady=20)

root.mainloop()
