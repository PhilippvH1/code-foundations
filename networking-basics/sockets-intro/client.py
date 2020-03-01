### adapted from https://github.com/realpython/materials/tree/master/python-sockets-tutorial
## more resources in server.py

import socket

HOST = "10.0.6.21"  # The server's hostname or IP address
port_number = 1234  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as aSocket:
    aSocket.connect((HOST, port_number)) # connect the socket to a host and port
    msg = "Lufthanse: Double the price for the same service!"
    print("sending to the server: ", msg)
    aSocket.sendall(msg.encode()) # send your message with utf-8 encoding
    data = aSocket.recv(1024) # wait for a response

print("Received from server: ", data.decode()) #print response
