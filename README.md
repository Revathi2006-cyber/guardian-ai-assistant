# Guardian AI Assistant 

A Python-based voice-controlled emergency assistant that detects distress voice commands using NLP and sends real-time WhatsApp alerts with the user’s location.

##  Features
- Voice command listening (Speech Recognition)
- Emergency phrase detection using NLP + Fuzzy Matching
- WhatsApp alert system via `pywhatkit`
- Location sharing using IP
- Emergency logging to text file

##  Technologies Used
- Python
- SpeechRecognition
- pyttsx3
- sounddevice
- fuzzwuzzy (NLP)
- pywhatkit
- requests

##  How to Run
1. Clone the repo
2. Install requirements:
   ```bash
   pip install -r requirements.txt
