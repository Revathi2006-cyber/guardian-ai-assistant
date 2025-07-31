# location.py

import requests

def get_location():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        coords = data.get("loc")  # e.g., "17.3850,78.4867"
        if coords:
            return f"https://www.google.com/maps?q={coords}"
        return "Location not found"
    except Exception as e:
        return f"Error: {e}"
