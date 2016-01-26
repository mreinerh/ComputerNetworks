import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 7070


sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

try:
    message = "Hello World"
    sock.sendto(message, (UDP_IP, UDP_PORT))
    print "Sent: " + message
except Exception as e:
    print e.message
finally:
    print "Goodbye"
    sock.close()