# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print("Socket successfully created")

port = 10001

s.bind(('192.168.1.100', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")


while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    c.send('Thank you for connecting'.encode())

    # Close the connection with the client
    # c.close()
    print(c.recv(100))
    # txt = "bhanu" + '\n'
    # msg = txt.encode("utf8")
    # s.sendall(msg)
