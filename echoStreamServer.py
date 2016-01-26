# QUICK QUESTION SQUAD, should the program exit if it receives nothing at all? Currently, it does. 

"""
Title:          Echo Server Program
Authors:        Alex Higgins, Matt Haneburger, Steven King, Tony Raubenheimer
Description:    Listens on assigned TCP port, 22600, for an input connection. The server echoes each _line_ of 
                input from the client, until it gets the line "exit" or "quit". 
"""

import socket
import sys

HOST = ''       #Constant variable that allows any host to connect
PORT = 22600    #Constant variable, which means client has to bind to port 22600 to connect

open_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
open_socket.bind((HOST, PORT))
open_socket.listen(15)
info, location = open_socket.accept()
print ("Receiving connection from {0}" .format(location))

while 1:
# This is an infinite loop, which loops indefinitely because we want to collect data until the data equals quit, exit, or no message at all.
    message = info.recv(1024)
    if not message:
    # if this matches anything other than a message, we break
        break
    elif (message == "quit"):
    # if the message equals quit, we print the quitting message, close the socket, and exit the loop
        print ("Received quit command. Quitting now")
        info.close()
        break
    elif (message == "exit"):
    # if the message equals exit, we print the exitting message, close the socket, and exit the loop
        print ("Recieved exit command. Exiting now")
        info.close()
        break
    else:
    # If the message contains some data that does not equal "quit" or "exit", we send that message
        print ("{0}" .format(message))
        info.sendall(message)
info.close()
