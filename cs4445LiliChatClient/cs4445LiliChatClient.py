#
#   Lili Valentine Holley
#

from socket import *
import pprint

#Create socket
serverSocket = socket(AF_INET, SOCK_STREAM)
HOST = '192.168.0.108'
PORT = 42790
serverSocket.connect((HOST, PORT))


#Create a username
while True:
    try:
        username = input('Type a username\n')
        usernameLength = len(username)
        if usernameLength > 40: #40 character length limit
            raise ValueError #this will send it to the print message and back to the input option
        username += ':'
        break
    except ValueError:
        print("Invalid username. Only 40 characters allowed.")

usernameBytes = username.encode()
usernameLengthBytes = str(usernameLength).encode()
welcomeMessage = 'is here!'
welcomeMessageLength = len(welcomeMessage)
welcomeMessageBytes = str(welcomeMessageLength).encode()

serverSocket.send(usernameLengthBytes + '\n'.encode() + welcomeMessageBytes + '\n'.encode() + usernameBytes + '\n'.encode() + welcomeMessage.encode())

while True:
    #Receive a list of all messages and only update new ones
    allMessages = []
    recv = serverSocket.recv(4096) #receives all messages from server
    newMessages = (recv.decode()).splitlines() #creates a list from each seperate line 
    updateMessages = list(set(newMessages) ^ set(allMessages)) #This seperates old messages from the new messages, which allows me to only show the new messages
    updateMessages.insert(0, updateMessages)
    pprint.pprint(updateMessages)
    allMessages = list(set(newMessages) | set(allMessages)) #This updates the new messages to the old messages, recycling the whole process

    message = input("Type your message\n")
    messageLength = len(message)
    messageBytes = message.encode()
    messageLengthBytes = str(messageLength).encode()

    serverSocket.send(usernameLengthBytes + '\n'.encode() + messageLengthBytes + '\n'.encode() + usernameBytes + '\n'.encode() + messageBytes)

