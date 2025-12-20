import socket
import threading
import sys
import argparse
from .client_handler import handle_client
   

def main():
    parser = argparse.ArgumentParser(description="Basic multi-client chat system")
    parser.add_argument(
        metavar="IPv4",
        dest="ip",
        help = "IP address of the system"
    )
    parser.add_argument(
        metavar="port",
        dest="port",
        type=int,
        help="Port to connect",
    )
    args = parser.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        s.bind((args.ip, args.port))
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