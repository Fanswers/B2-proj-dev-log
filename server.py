import socket
import sys
from _thread import *
from datetime import datetime

HOST = ''
PORT = 25565


# Creation du socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à une adresse précise :
try:
    mySocket.bind((HOST,PORT))
except socket.error as e:
    print("La liaison du socket à échouée.", str(e))
    sys.exit()

while 1:
    # Attente de la requête de connexion d'un client
    print("En attente de requêtes")
    mySocket.listen(2)

    # Etablissement de la connexion
    connexion, addresse = mySocket.accept()
    date = datetime.now()
    print("Client connecté, adresse IP %s, port %s" % (addresse[0], addresse[1]), date)

    # Dialogue avec le client
    while 1:
        msgClient = connexion.recv(1024)
        print("C>", msgClient.decode())
        if msgClient.upper() == "FIN" or msgClient.decode() == "deconnexion":
            by = "Au revoir !"
            connexion.sendto(by.encode(), (HOST, PORT))
            print("connexion interrompue.")
            connexion.close()
            break
        msgServeur = input("S> ")
        connexion.sendto(msgServeur.encode(), (HOST, PORT))
        msgClient = connexion.recv(1024)
