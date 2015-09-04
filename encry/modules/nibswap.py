import binascii, argparse

parser = argparse.ArgumentParser(description='Reverses the nibble array of a specified file')

parser.add_argument('-i','--input', help='Input file name', required=True)
parser.add_argument('-o','--output', help='Output file name', required=True)
args=parser.parse_args()

data=open('%s' % args.input,'rb').read() #open file to read
data2=binascii.hexlify(data) #convert bytes to hex

with open('%s' % args.output,'wb') as output: #open file to write
  output.write(binascii.unhexlify(''.join(reversed(data2)))) #write file in reverse bytes

