import socket,base64

host='127.0.0.1'
port=5555

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect((host,port))

data=conn.recv(256).split("\n")
conn.send(base64.b64decode(data[2]))
data2=conn.recv(256).split("\n")
conn.send(base64.b32decode(data2[2]))
data3=conn.recv(256).split("\n")
conn.send(base64.b16decode(data3[2]))
print (conn.recv(256))

