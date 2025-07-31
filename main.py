# main.py

import time
from voice import listen, detect_emergency, speak
from alert import send_whatsapp_alert
from config import EMERGENCY_CONTACT, DEFAULT_MESSAGE
from location import get_location
from logger import log_emergency

def main():
    speak("Guardian Assistant is now active. Say your emergency command anytime.")

    while True:
        command = listen()

        if command:
            if detect_emergency(command):
                speak("Emergency detected. Sending WhatsApp alert now.")
                location_link = get_location()

                full_message = f"{DEFAULT_MESSAGE}\nVoice Command: '{command}'\nLocation: {location_link}"
                send_whatsapp_alert(EMERGENCY_CONTACT, full_message)
                log_emergency(command, location_link)
            else:
                speak("No emergency detected. You're safe.")
        else:
            speak("No input received.")

        time.sleep(5)  # Pause before listening again

if __name__ == "__main__":
    main()