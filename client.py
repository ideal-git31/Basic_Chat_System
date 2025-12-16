import socket 
import threading 
import sys
import time

def send_msg(s):
    while True:
        try:
            msg = input("")
            if msg.lower() == "exit":
                s.send(msg.encode())
                print("Client Exiting...")
                s.close()
                break
            s.send(msg.encode())
        except (BrokenPipeError, OSError):
            break
        except KeyboardInterrupt:
            s.send("exit".encode())
            break
    sys.exit(0)    


def recieve_msg(s):
    while True:
        try:
            msg = s.recv(1024)

            if not msg:
                print("Connection closed by server.")
                break

            if msg.decode() == "exit": 
                print("Connection closed by the server..")
                break

            print(f"Server: {msg.decode()}") 
        except OSError:
            break
        except KeyboardInterrupt:
            break    

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        try:
            s.connect(("127.0.0.1", 12345))
            break
        except (ConnectionRefusedError, OSError):
            time.sleep(1)
        except KeyboardInterrupt:
            print("Client Interuppted. Exiting..")
            sys.exit(0)    

    print("CONNECTED TO THE SERVER...")  

    t1 = threading.Thread(target = send_msg, args=(s,), daemon=True)
    t2 = threading.Thread(target = recieve_msg, args=(s,), daemon=True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    try:
        s.close()
    except:
        pass

    print("Client Closed.")    
    
if __name__ == "__main__":
    main()