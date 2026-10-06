import socket

server = socket.socket()
server.bind(("127.0.0.1",9000))
server.listen(1)
print("Echo server waiting....")
conn,addr = server.accecpt()
while True:
    data = conn.recv(1024)
    
    if not data:
        break
    conn.sendall(data)
conn.close()
server.close()
