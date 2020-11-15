# Big, no sockets, no Sockers tutorial

## Initialising Modules
```
import sockets
import threading #threading allows form different lines of code to be executed seperatly from each other
```

## Sever.py
```
import socket
import threading #threading alows different lines of code to run independetly

HEADER = 64 #setting first message protocal
PORT = 5050 #port commonly used
SERVER = socket.gethostbyname(socket.gethostname()) #getting the host's local ip
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #intialising a socket with the internet, with the stream parameter
server.bind(ADDR) #binding the socket to an adress the sever and the respective port

def handle_client(conn, addr): #Client handler, will run for each client
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msgLength = conn.recv(HEADER).decode(FORMAT) #waits to recieve a message from a client, decodes it from bytes to utf-8 string
        msgLength = int(msgLength)
        msg = conn.recv(msgLength).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE: #if disconnect message is evoked
            connected = False #exit the loop
        print(f"[{addr}] {msg}")
    conn.close() #disconnecting the user

def start(): #Initialise the sever
    server.listen() #listiening for connections
    print(f"[LISTENING] Server active on {SERVER}")
    while True:
        conn, addr = server.accept() #storing the connectors information
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #creating a new thread of the client, with there information
        thread.start() #starting the thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") #tells how many threads are active, how mant clients, minuce the start thread

print("[INITIALISING] Server is starting")
start()
```