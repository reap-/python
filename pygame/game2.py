import socket,multiprocessing

host=""
port=5555

def game(conn): 
  print '[*] Connected tp', addr

data=open('pic.png','rb').read()
print data



if __name__ == "__main__":
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.bind((host,port))
  s.listen(3)
  print '[*] Listening on port %s:%d' % (socket.gethostbyname(socket.gethostname()), port)
  while 1:
    conn, addr=s.accept()
    newclient=multiprocessing.Process(target = game, args = (conn, ))
    newclient.start()
