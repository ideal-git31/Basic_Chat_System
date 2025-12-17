from .state import state
def broadcast(message, sender_socket=None):
    for client in list(state.clients.keys()):
        if client != sender_socket:
            try:
                client.send(message.encode())
            except Exception as e:
                print("[BROADCAST ERROR]", e)   