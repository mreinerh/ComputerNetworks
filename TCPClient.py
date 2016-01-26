import socket

HOST = '172.17.149.120'    # The remote host
PORT = 22600              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print "Enter a command to be forwarded:"

while 1:
  userInput = raw_input()
  if (userInput == quit):
    print "Quitting now"
    s.close()
  elif (userInput == exit):
    print "Exiting now"
    s.close()
  else:
    s.send(userInput)
    data = s.recv(1024)
  #print 'Received', repr(data)
