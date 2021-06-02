import socket
import sys

class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.1.73'
        self.port = 25565
        self.addresse = (self.host, self.port)

    def connect(self):
        try:
            self.client.connect(self.addresse)
        except socket.error as e:
            print("La connextion a échoué",str(e))
        print("connexion établie avec le serveur")

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)

    def disconnect(self):
        self.client.close()