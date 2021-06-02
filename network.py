import socket
from datetime import datetime

class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.1.73" # Entrer l'addresse IPv4 public
        self.port = 25565           # Port ouvert sur la Box
        self.addr = (self.host, self.port)
        self.log1 = input("nom de compte : ")
        self.log2 = input("mot de passe : ")
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        self.client.sendall(str.encode(self.log1 + ',' + self.log2))
        print(self.client.recv(2048).decode())
        return self.client.recv(2048).decode()

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)
