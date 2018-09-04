import socket
import sys
from random import shuffle


class ServerSplitter:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening = False

    def start_listening(self):
        self.s.bind(("0.0.0.0", int(sys.argv[1])))
        self.s.listen(5)
        self.listening = True
        while self.listening:
            (client_socket, address) = self.s.accept()
            try:
                data = client_socket.recv(1024).decode("utf-8").split(" ")
                shuffle(data)
                print(data)
                client_socket.send(" ".join(data).encode("utf-8"))
                client_socket.shutdown(socket.SHUT_RDWR)
                client_socket.close()
            except Exception as e:
                print(e)


if __name__ == "__main__":
    splitter = ServerSplitter()
    splitter.start_listening()
