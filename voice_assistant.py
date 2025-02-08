import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import time
import webbrowser

# Initialize the speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice for text-to-speech output
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index if you want a different voice

def talk(text):
    """Convert text to speech and output it."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen and recognize the user's voice command."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)  # Adjust microphone sensitivity
            voice = listener.listen(source, timeout=5)  # Listen with a timeout for efficiency
            command = listener.recognize_google(voice)  # Convert speech to text
            command = command.lower()
            print(f"Recognized: {command}")  # Debugging print statement
            return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you repeat?")
        return None
    except sr.RequestError:
        print("Sorry, there seems to be an issue with the speech recognition service.")
        return None

def get_weather():
    """Fetch and report the weather for a specified city using OpenWeatherMap API."""
    api_key = "{YOUR_API_KEY}"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    talk("Which city's weather would you like to check?")
    city = take_command()

    if city:
        complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
        response = requests.get(complete_url)
        data = response.json()

        if data.get("cod") == 200:  # Check if request was successful
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"]
            talk(f"The current temperature in {city} is {temp}°C with {weather_desc}.")
        else:
            talk("Sorry, I couldn't fetch the weather details. Please try again.")
    else:
        talk("I didn't catch the city name. Please try again.")

def set_reminder():
    """Set a simple reminder that repeats after a short delay for demonstration."""
    talk("What would you like to be reminded about?")
    reminder = take_command()
    talk("When should I remind you?")
    reminder_time = take_command()

    if reminder and reminder_time:
        talk(f"Reminder set: {reminder} at {reminder_time}.")
        time.sleep(5)  # Simulating the passage of time for testing
        talk(f"Reminder: {reminder} at {reminder_time}.")
    else:
        talk("I didn't catch the details. Please try again.")

def run_alphachat():
    """Main function to process user commands and perform the requested tasks."""
    command = take_command()

    if command is None:
        talk("I didn't hear you. Can you say that again?")
        return

    # Ensure the command is properly formatted
    command = command.strip()

    if 'play' in command:
        # Play a YouTube video for a requested song or topic
        song = command.replace('play', '').strip()
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        # Get and announce the current time
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time_now}")

    elif 'weather' in command:
        # Fetch and announce weather details
        get_weather()

    elif 'set a reminder' in command:
        # Set a reminder
        set_reminder()

    elif 'search for' in command:
        # Search Google for the requested query
        query = command.replace('search for', '').strip()
        talk(f"Searching Google for {query}")
        pywhatkit.search(query)

    elif 'open' in command:
        # Open a website in the default web browser
        site = command.replace('open', '').strip()
        talk(f"Opening {site}")
        webbrowser.open(f"https://{site}.com")

    elif 'joke' in command:
        # Tell a joke
        talk(pyjokes.get_joke())

    elif 'bye' in command or 'exit' in command:
        # Exit the assistant
        talk('Goodbye! Have a great day!')
        exit()

    else:
        talk("Sorry, I didn't understand that. Please try again.")

# Run the assistant in an infinite loop to continuously listen for commands
while True:
    run_alphachat()
