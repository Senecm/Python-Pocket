import socket

HEADER = 64 
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT" 
#client unique
SERVER = "" #github
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) #encodes message in bytes
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength += b' ' * (HEADER - len(sendLength)) #padds the object so it fits the message protocol
    client.send(sendLength)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))

send("Gun")
input("") #makes user presss enter before next message is send
send("BIG BIG BIG BIG")
input()
send(DISCONNECT_MESSAGE)