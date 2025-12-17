import socket 
import threading 
import sys
import time
from .sender import send_msg
from .reciever import recieve_msg

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

    srvr_msg = s.recv(1024).decode()
    print(srvr_msg + " ")
    username = input()
    s.send(username.encode())

    print(f"Welcome {username} to the chat! Type 'SIGNING OFF' to leave.")

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