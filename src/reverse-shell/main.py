import socket

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
                        print("[*] Waiting for response...")
                        
                        output = b""
                        delimiter = b"\n<<<END_OF_OUTPUT>>>\n"
                        
                        while True:
                            chunk = conn.recv(4096)
                            if not chunk:
                                print("[!] Connection lost")
                                break
                            output += chunk
                            print(f"Total bytes: {len(output)}, Last 50 chars: {output[-50:]}")
                            if delimiter in output:
                                break
                        
                        if delimiter in output:
                            output = output.split(delimiter)[0]
                            print(output.decode())
                        else:
                            print("[!] Incomplete output received")
                        
            except (BrokenPipeError, ConnectionResetError):
                print("[!] Client disconnected unexpectedly")
            
            print("[*] Waiting for new connection...")
            
    except KeyboardInterrupt:
        print("\n[!] Shutting down...")
    finally:
        server.close()

if __name__ == "__main__":
    listen()