#!/usr/bin/python
import socket,time,struct,sys,random

planet_earth = 'alive'

def recv_timeout(conn,hit,timeout=.05):
  conn.setblocking(0)
  total_data=[];
  data='';
  begin=time.time()
  while 1:
    if total_data and time.time()-begin > timeout:
      print '[+] got hit on %s ... data returned : %s ' % (repr(hit),total_data)
      exit()
      break
    elif time.time()-begin > timeout*2:
      break
    try:
      data = conn.recv(8192)
      if data:
        total_data.append(data)
        begin=time.time()
      else:
        time.sleep(0.1)
    except:
      pass
  return ''.join(total_data)

def fuzz_struct():
  i = 0
  while planet_earth == 'alive':
#    data = hex(i)[2:].zfill(2)
    conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.connect((host,port))
    pack = struct.pack('h', i)
    conn.send(pack)
    recv_timeout(conn,pack)
    print '[+] Sent : ', repr(pack), ' || Got : ', recv_timeout(conn).strip()
    conn.close()
    i += 1

def fuzz_array():
  i = 0
  while i != 255:
    data = hex(i)[2:].zfill(2)
    conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.connect((host,port))
    conn.send(bytearray.fromhex(data))
    recv_timeout(conn,data)
    print '[+] Sent : ', repr(data), ' || Got : ', recv_timeout(conn).strip()
    conn.close()
    i += 1

def fuzz_random():
  while planet_earth == 'alive':
    i = random.randint(0,32)
    rando = open('/dev/urandom','rb').read(i)
    conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.connect((host,port))
    conn.send(rando)
    recv_timeout(conn,rando)
    print '[+] Sent : ', rando.encode('hex'), ' || Got : ', recv_timeout(conn).strip()
    conn.close()


if len(sys.argv)<2:
  print '[*] Usage : fuzz.py <ip> <port>'
  sys.exit()
else:
  host=sys.argv[1]
  port=int(sys.argv[2])
  fuzz_array()
  fuzz_struct()
  fuzz_random()
