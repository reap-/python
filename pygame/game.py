import socket,base64,string,random,time,signal,multiprocessing

host=""
port=5555

class AlarmException(Exception):
  pass

def alarm_handler(signum,frame):
  conn.send('\n\nSlow Poke, just not fast enough!\n\n')
  raise AlarmException

def game(conn):
  key1=base64.b16encode(''.join(random.sample(['Base64','encoding','schemes','are','commonly','used','when','there','is','a','need','to','encode'],5)))
  key2=base64.b32encode(key1)
  key3=base64.b64encode(key2)
  signal.signal(signal.SIGALRM,alarm_handler)
  print '[*] Connected tp', addr
  conn.send('Its all about the base, bout the base\nYou have 2 seconds to decode the following\n%s\n'% key3)
  conn.send('Your Input?: ')
  try:
    signal.alarm(2)
    data=conn.recv(128)
    if data.rstrip()==base64.b64decode(key3):
      conn.send("\nCorrect!  How about this?\n%s\n"% key2)
      data2=conn.recv(128)
      if data2.rstrip()==base64.b32decode(key2):
        conn.send("\nCorrect again!  Last one I promise...\n%s\n"% key1)
        data3=conn.recv(128)
        print(data3)
        if data3.rstrip()==base64.b16decode(key1):
          response="\nAMazing you deserve a cookie and a flag!"
          conn.send(response)
          conn.close()
        else:
          response="Close but no cigar\n"
#          conn.send(response)
      else:
        response="Nice try pal!SAA\n"
    else:
      response="Wrong.... try another guess\n"
    conn.send(response)
    print '[*] Process terminated, closing connection to', addr
    conn.close()

  except:
    print '[*] Process terminated, closing connection to', addr
    conn.close()

if __name__ == "__main__":
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.bind((host,port))
  s.listen(3)
  print '[*] Listening on port %s:%d' % (socket.gethostbyname(socket.gethostname()), port)
  while 1:
    conn, addr=s.accept()
    newclient=multiprocessing.Process(target = game, args = (conn, ))
    newclient.start()
