import socket
hote = "localhost"
port = 12397

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))

print("Connexion établie avec le serveur sur le port {}".format(port))
msg_a_envoyer = ""
while msg_a_envoyer != "fin":
    msg_a_envoyer = input("> ")
    connexion_avec_serveur.send(msg_a_envoyer.encode("Utf8"))
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode())

print("Fermeture de la connexion")
connexion_avec_serveur.close()
