import socket
import threading


def check_path(line):
    return line.split(" ")[1] == "/"


def check_GET(string):
    return "GET" in string


def get_http_ver(string):
    return string.split(" ")[-1]


def get_host_ver(data):
    for line in data:
        if "Host" in line:
            return line.split(" ")[-1]


def get_agent_ver(data):
    for line in data:
        if "User-Agent" in line:
            return line.split(" ")[-1]


class RequestConsumer(threading.Thread):

    def __init__(self, client_socket, address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.address = address

    def run(self):
        try:
            data = self.client_socket.recv(1024).decode("utf-8").splitlines()
            if check_GET(data[0]) and check_path(data[0]):
                http_ver = get_http_ver(data[0])
                host_str = get_host_ver(data)
                user_str = get_agent_ver(data)
                response = ["%s 200 OK" % http_ver, "Content-Type: text/html;", ""]
                with open("../resources/index.html", "r") as content_file:
                    response.append(content_file.read())
                self.client_socket.send("\n".join(response).encode("utf-8"))
                self.client_socket.shutdown(socket.SHUT_RDWR)
                self.client_socket.close()
        except Exception as e:
            print(e)


class Server:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening = False
        self.threads = []

    def start_listening(self):
        self.s.bind(("0.0.0.0", 8080))
        self.s.listen(5)
        self.listening = True
        while self.listening:
            a, b = self.s.accept()
            thread = RequestConsumer(a, b)
            thread.start()
            self.threads.append(thread)

    def stop_listening(self):
        self.listening = False
        for thread in self.threads:
            thread.join()
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()


if __name__ == "__main__":
    splitter = Server()
    splitter.start_listening()
    input("Press enter to stop the server...")
