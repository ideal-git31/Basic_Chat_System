import socket
import threading
import sys

def send_msg(client):
    while True:
        try:
            msg = input("")
            if msg.lower() == "exit":
                client.send(msg.encode())
                client.close()
                break
            client.send(msg.encode())
        except (BrokenPipeError, OSError):
            break
        except KeyboardInterrupt:
            client.send("exit".encode())
            break
    sys.exit(0)

def recieve_msg(client):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                print("Connection cloced by client.")
                break
            if msg.decode() == "exit":
                print("Connection closed by the client.")
                break

            print(f"Client: {msg.decode()}")  
        except  OSError:
            break
        except KeyboardInterrupt:
            break      

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind(("127.0.0.1", 12345))
        print("LISTENING........ on port 12345")
        s.listen(1)

        client, addr = s.accept() 
        print(f"Connected to {addr}")

        t1 = threading.Thread(target = send_msg, args=(client,), daemon=True)
        t2 = threading.Thread(target = recieve_msg, args=(client,), daemon=True)
        
        t1.start()
        t2.start()

        t1.join()
        t2.join()
    except KeyboardInterrupt:
        print("\nServer Interupttted. Exiting...")
    finally:
        try:
            client.close()
        except:
            pass
        s.close()
        print("Server Closed.")

if __name__ == "__main__":
    main()