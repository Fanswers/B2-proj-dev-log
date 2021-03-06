import socket
from _thread import *
import sys
from datetime import datetime
import BDD

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.1.4'
port = 9991
server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
grille2 = ["0:[0,0,0,0,0,0,0,0,0]/0","1:[0,0,0,0,0,0,0,0,0]/0"]


def threaded_client(conn,):
    global currentId, pos, grille2
    logs = conn.recv(2048).decode('utf-8')
    log1 = logs.split(',')[0]
    log2 = logs.split(',')[1]
    print("log1: ", log1, " log2: ", log2)
    if BDD.Connection(log1, log2) == False:
        print("mauvais login/password client")
        conn.close()
        return 0
    else:
        conn.sendall(str.encode("Vous êtes connectés"))
    conn.sendall(str.encode(currentId))
    currentId = "1"
    reply = ''

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.sendall(str.encode("Goodbye"))
                break
            else:
                #print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                grille2[id] = reply

                if id == 0: nid = 1
                if id == 1: nid = 0

                reply = grille2[nid][:]
                #print("Sending: " + reply)
            conn.sendall(str.encode(reply))
        except:
            break
    grille2 = ["0:[0,0,0,0,0,0,0,0,0]/0","1:[0,0,0,0,0,0,0,0,0]/0"]
    print("Connection Closed")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    print("connect", datetime.now())

    start_new_thread(threaded_client, (conn,))