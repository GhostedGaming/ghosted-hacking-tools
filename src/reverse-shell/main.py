import socket
from os import system

def listen():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("[*] Socket created")
    
    server.bind(('0.0.0.0', 8080))
    print("[*] Server bound to 0.0.0.0:8080")
    
    server.listen(1)
    print("[*] Listening for connections...")
    
    try:
        while True:
            conn, addr = server.accept()
            print(f"[+] Connection received from {addr}")
            
            try:
                while True:
                    msg = input("> ")
                    if msg.lower() == "exit":
                        print("[*] Exiting...")
                        conn.close()
                        return
                    elif msg.lower() == "disconnect":
                        print("[*] Disconnecting client...")
                        conn.close()
                        break
                    else:
                        conn.sendall(msg.encode())
                        print("[*] Command sent")
            except (BrokenPipeError, ConnectionResetError):
                print("[!] Client disconnected unexpectedly")
            
            print("[*] Waiting for new connection...")
            
    except KeyboardInterrupt:
        print("\n[!] Shutting down...")
    finally:
        server.close()

if __name__ == "__main__":
    listen()