import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "c6a30600513640e5ba51fa9ca57d5237"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    apikey = "AIzaSyAFfFRRwqNKTOG7ACZtR1xXXnzKln7EcFg"

    genai.configure(api_key = apikey)
    model = genai.GenerativeModel("gemini-1.5-flash")

    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )

    response = model.generate_content(command)
    return response.text

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        songs = c.lower().split(" ")[1]
        link = musicLibrary.music[songs]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=c6a30600513640e5ba51fa9ca57d5237")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let openAi handle it 
        output = aiProcess(c)
        speak(output)
        pass
        
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    # Listen for the wake word "Jarvis"
    while True:
        r = sr.Recognizer()
        
        print("Recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Sir")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processcommand(command)
                    
        except Exception as e:
            print("Jarvis error; {0}".format(e))