from .state import state
from .broadcaster import broadcast

def handle_client(client, addr):
    try:
        client.send("Enter username: ".encode())
        username = client.recv(1024).decode().strip()

        state.clients[client] = username
        print(f"{username} joined from {addr}")
        broadcast(f"{username} has joined the chat!")

        while True:
            raw_msg = client.recv(1024)
            if not raw_msg:
                break

            msg = raw_msg.decode().strip()

            if msg.lower() == "signing off":
                broadcast(f"{username} has signed off from the chat.")
                break

            broadcast(f"{username}: {msg}", sender_socket=client)

    except Exception as e:
        print("[ERROR]",e)
    finally:
         state.clients.pop(client, None)
         client.close()           
