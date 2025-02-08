# Voice Assistant

It is a Python-based voice assistant that recognizes spoken commands and performs various tasks such as playing YouTube videos, telling the time, fetching weather updates, setting reminders, searching Google, opening websites, and telling jokes.

## Features
- **Play YouTube Videos**: Say "Play [song name]" to play a song on YouTube.
- **Check Time**: Ask "What time is it?" to get the current time.
- **Get Weather Updates**: Say "Weather" to check the weather for a specific city.
- **Set Reminders**: Say "Set a reminder" and provide details to set a basic reminder.
- **Search Google**: Say "Search for [query]" to look up information on Google.
- **Open Websites**: Say "Open [website name]" to launch a website.
- **Tell Jokes**: Say "Tell me a joke" for some humor.
- **Exit the Assistant**: Say "Bye" or "Exit" to close the program.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.x recommended). Install the required libraries using:
```sh
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes requests
```

## Usage
Run the script with:
```sh
python voice_assistant.py
```
Speak your commands clearly when prompted. The assistant will recognize your voice and respond accordingly.

## API Requirements
- To fetch weather updates, replace the `api_key` in `get_weather()` with your OpenWeatherMap API key.

## Troubleshooting
- Ensure your microphone is working properly.
- If the assistant doesn’t recognize your voice, try adjusting the noise level using `listener.adjust_for_ambient_noise(source)`.
- If speech recognition fails, check your internet connection as Google Speech API requires connectivity.

## License
This project is open-source and available under the MIT License.

