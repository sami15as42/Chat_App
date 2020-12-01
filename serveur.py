import socket

hote =  ''
port = 12397

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))

connexion_principale.listen(3)

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    print(msg_recu.decode())
    connexion_avec_client.send(b"5 / 5")
print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
