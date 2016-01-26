#echo server program
import socket
import sys

HOST = ''
PORT = 22600

ourSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ourSocket.bind((HOST, PORT))
ourSocket.listen(15)
info, location = ourSocket.accept()
print ("Receiving connection from {0}" .format(location))

while 1:
    message = info.recv(1024)
    if not message:
        break
    elif (message == "quit"):
        print ("Received quit command. Quitting now")
        info.close()
        break
    elif (message == "exit"):
        print ("Recieved exit command. Exiting now")
        info.close()
        break
    else:
        print ("{0}" .format(message))
        info.sendall(message)
info.close()