import socket

#Network Info
UDP_IP = "127.0.0.1"
UDP_PORT = 7070

#Create a new Dgram socket
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

#Try to send a message over the socket.
try:
    message = "Hello World"
    sock.sendto(message, (UDP_IP, UDP_PORT))
    print "Sent: " + message
except Exception as e: #Print an error, if there is any
    print e.message
finally: #Close the socket
    print "Goodbye"
    sock.close()