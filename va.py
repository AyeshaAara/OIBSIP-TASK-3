import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the speech engine for text-to-speech conversion
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    
    # Use the microphone as the source of audio
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        # Convert speech to text using Google Speech Recognition
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, I couldn't connect to the speech service.")
        return None

# Function to respond based on the recognized speech
def respond(query):
    if query is None:
        return
    
    # Check if the query contains specific words and respond accordingly
    if 'hello' in query:
        speak("Hello! How can I assist you today?")
    
    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    
    elif 'date' in query:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    
    elif 'exit' in query or 'bye' in query:
        speak("Goodbye! Have a great day.")
        exit()
    
    else:
        speak("I'm sorry, I don't understand that request.")

# Main loop to keep the assistant running
def run_assistant():
    speak("Hello, I am your assistant. How can I help you?")
    
    while True:
        query = listen()  # Listen to the user input
        if query:
            respond(query)  # Process the query and respond

# Run the assistant
if __name__ == "__main__":
    run_assistant()
