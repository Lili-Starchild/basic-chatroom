#
#   Lili Valentine Holley
#

from socket import *
import _thread

allMessages = [] #Global variable for remembering all past messages and users

#Creates a way for multiple clients to connect at once
def client_connected(connectionSocket, addr):
    while True:
        try: #This section collects the username and message sent from client and updates it to a global list of all messages
            recv = (connectionSocket.recv(1024)).decode()
            recvLines = recv.splitlines()
            usernameLength = recvLines[0]
            messageLength = recvLines[1]
            username = recvLines[2]
            del recvLines[:2]
            allMessages.append(recvLines)
            message = recvLines[1:]
            print(username + str(message))
            connectionSocket.send(str(allMessages).encode())
        except :
            connectionSocket.close()
            print(username + "has left the server.\n")
            allMessages.append(username + "has left the server.\n")
            break

#Create socket and bind
serverSocket = socket(AF_INET, SOCK_STREAM)
HOST = 'localhost'
PORT = 42790
serverSocket.bind((HOST, PORT))

#Open chat room and accept connections
print("Chat room is open.\n")
serverSocket.listen()
while True:
    c, addr = serverSocket.accept()
    _thread.start_new_thread(client_connected,(c,addr)) #Passes the accepted client to their own thread
serverSocket.close()
