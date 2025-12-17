import socket
import threading
import sys
from .client_handler import handle_client
   

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        s.bind(("127.0.0.1", 12345))
        print("Server started at port 12345")
        s.listen(5)

        while True:
            client, addr = s.accept()
            print(f"New connection from {addr}")
            threading.Thread(target=handle_client,
                              args=(client, addr),
                              daemon=True
                              ).start()

    except KeyboardInterrupt:
        print("\nServer is shutting down.")    
    finally:
        s.close()        

if __name__ == "__main__":
    main()