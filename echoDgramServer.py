import socket
import sys

#Network Info
UDP_IP = "127.0.0.1"
UDP_PORT = 7070

#Create a new Dgram socket
sock = socket.socket(socket.AF_INET,#Internet
                       socket.SOCK_DGRAM)#Specify Datagram
#Try to bind it to a port
try:
    sock.bind((UDP_IP,UDP_PORT))
    print "Socket bound to: " + UDP_IP + ":" + str(UDP_PORT)
except Exception as e: #If there is an error, print the error
    print e
    sys.exit(1)

#Listen until a connection is made. Print out the data and address, then exit.
while True:
    data, addr = sock.recvfrom(2048)#Buffer size
    print "Data: " + data
    print "Addr: " + str(addr)
    print 'Goodbye!'
    sys.exit(0)
    '''if(str(data).lower() == 'exit' or str(data).lower() == 'quit'):
        print "Goodbye!"
        sock.close()
        sys.exit(0)'''