import argparse


#def brute(array):











parser = argparse.ArgumentParser(description='XOR a File')
parser.add_argument('-i','--input', help='Input file name', required=True)
parser.add_argument('-o','--output', help='Output file name', required=True)
parser.add_argument('-x','--xor', type=int, help='Value to XOR file with', required=True)
args=parser.parse_args()
xor=args.xor
original=open('%s' % args.input,'rb')
array=bytearray(original.read())
print array
encrypted=bytearray([b^xor for b in bytearray(array)])
print encrypted
for i in range(255):
  print '[*] Trying XOR value : %s' % i
  brute=bytearray([b^i for b in bytearray(encrypted)])
  print brute
newfile=open('%s' % args.output,'wb')
newfile.write(encrypted)
