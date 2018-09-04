import socket
import sys

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.connect((sys.argv[1], int(sys.argv[2])))
        server_socket.send(b'super califragilisti che spiralidoso')
        print(server_socket.recv(1024).decode("utf-8"))
    except Exception as e:
        print(e)
    finally:
        server_socket.close()
