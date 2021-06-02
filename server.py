import socket
from _thread import *
import sys
from datetime import datetime
import BDD

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.1.73'
port = 25565
server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = ["0:50,50", "1:100,100"]
grille2 = ["0:[0,0,0,0,0,0,0,0,0]","1:[0,0,0,0,0,0,0,0,0]"]


def threaded_client(conn,):
    global currentId, pos, grille
    logs = conn.recv(2048).decode('utf-8')
    log1 = logs.split(',')[0]
    log2 = logs.split(',')[1]
    print("log1: ", log1, " log2: ", log2)
    if BDD.Connection(log1, log2) == False:
        print("mauvais login/password client")
        conn.close()
        return 0
    else:
        conn.send(str.encode("Vous êtes connectés"))
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                grille2[id] = reply

                if id == 0: nid = 1
                if id == 1: nid = 0

                reply = grille2[nid][:]
                print("Sending: " + reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Connection Closed")
    conn.close()


while True:
    conn, addr = s.accept()
    print("connect", datetime.now())
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))