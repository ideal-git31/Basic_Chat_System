import os
def recieve_msg(sock):
    while True:
        try:
            msg = sock.recv(1024)

            if not msg:
                print("Connection closed by server.")
                sock.close()
                os._exit(0)
                break

            if msg.decode() == "signing off": 
                print("Connection closed by the server..")
                sock.close()
                os._exit(0)
                break

            print(f"{msg.decode()}") 
        except OSError:
            break
        except KeyboardInterrupt:
            break 