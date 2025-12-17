import sys

def send_msg(sock):
    while True:
        try:
            msg = input("")
            if msg.lower() == "signing off":
                sock.send(msg.encode())
                print("Client signed off...")
                sock.close()
                break
            sock.send(msg.encode())
        except (BrokenPipeError, OSError):
            break
        except KeyboardInterrupt:
            sock.send("SIGNING OFF".encode())
            break
    sys.exit(0)    