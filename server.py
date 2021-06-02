import socket
import queue
from _thread import *
from datetime import datetime
import sys


q = queue.Queue()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.1.4'
port = 25565
server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = 0
grille2 = ["0:[0,0,0,0,0,0,0,0,0]/0","1:[0,0,0,0,0,0,0,0,0]/0"]

def threaded_client(conn,):
    global currentId, pos, grille
    date = datetime.now()
    print(date)
    conn.send(str.encode(str(currentId)))
    currentId += 1
    q.put(currentId)
    print(q.qsize())
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                # print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                grille2[id] = reply

                if id == 0: nid = 1
                if id == 1: nid = 0

                reply = grille2[nid][:]
                # print("Sending: " + reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Connection Closed")
    conn.close()




def waiting_file(q):
    while q.qsize() > 2:
        q.get()
        q.get()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn,))