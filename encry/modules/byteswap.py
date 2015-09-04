import argparse

parser = argparse.ArgumentParser(description='Reverses the bytearray of a specified file')

parser.add_argument('-i','--input', help='Input file name', required=True)
parser.add_argument('-o','--output', help='Output file name', required=True)
args=parser.parse_args()

data=open('%s' % args.input,'rb')
array=bytearray(data.read())

array.reverse()

newfile=open('%s' % args.output,'wb')
newfile.write(array)
