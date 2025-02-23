import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime

class Jarvis:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening..")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen (source)
        try:
            command = self.recognizer.recognize_google(audio).lower()
            print("You:", command)
            return command
        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't understand that.")
            return""
        except sr.RequestError:
            self.speak("Speech recognition service is unavailable.")
            return ""
    
    def execute_command(self, command):
        if "opne notepad" in command:
            self.speak("Opening Notepad")
            os.system("notepad")
        elif "open browser" in command:
            self.speak("Opening browser")
            webbrowser.open("https://www.google.com")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            self.speak(f"The current time is {now}")
        elif "exit" in command or "quit" in command:
            self.speak("Goodbye!")
            exit()
        else:
            self.speak("Command not recognized.")
        
    def run(self):
        self.speak("Hello, I am Jarvis . How can I assist you?")
        while True:
            command = self.listen()
            if command:
                self.execute_command(command)

if __name__ == "__main__":
    assistant = Jarvis()
    assistant.run()

