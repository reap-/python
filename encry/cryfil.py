import argparse,binascii
import sys

def byte(args):
  print '[*] shaking all your bits of bytes around in the cookie jar....'
  data=open('%s' % args.input,'rb')
  array=bytearray(data.read())
  array.reverse()
  newfile=open('%s' % args.output,'wb')
  newfile.write(array)
  print '[*] job done'

def nibble(args):
  print '[*] tossin that giant bag of nibs around until it makes... kindof sense'
  data=open('%s' % args.input,'rb').read() 
  data2=binascii.hexlify(data)
  with open('%s' % args.output,'wb') as output:
    output.write(binascii.unhexlify(''.join(reversed(data2))))
  print '[*] job done.'

def xor(args):
  print '[*] addin these bits with your bits to make new bits...'
  xord=args.xor
  data=open('%s' % args.input,'rb')
  array=bytearray(data.read())
  with open ('%s' % args.output,'wb') as output:
    output.write(bytearray([b^xord for b in bytearray(array)]))
  print '[*] job done.'

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description='CryFil v1.\n\nGiving differant options to encrypt files on the fly..')
parser.add_argument('-i','--input', help='Input file name', required=True)
parser.add_argument('-o','--output', help='Output file name', required=True)
parser.add_argument('-b','--byte', help='Use to swap bytes', action='store_true')
parser.add_argument('-n','--nibble', help='Use to swap bytes', action='store_true')
parser.add_argument('-x','--xor', type=int, help='Value to XOR file with [0-255]')
if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)
args=parser.parse_args()

if args.byte:
  byte(args)
if args.nibble:
  nibble(args)
if args.xor:
  xor(args)
