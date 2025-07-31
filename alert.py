import pywhatkit
import pyautogui
import time

def send_whatsapp_alert(phone_number, message):
    print(f"Sending WhatsApp message instantly to {phone_number}...")

    try:
        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=20, tab_close=False)
        
        # Wait extra time to ensure the message box is ready
        print("Waiting before pressing Enter...")
        time.sleep(20)

        pyautogui.press('enter')  # Send message
        print("Message sent automatically!")

    except Exception as e:
        print(f"Error sending message: {e}")
