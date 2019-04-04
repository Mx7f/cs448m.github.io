import sys
from pyembroidery import read, write

if len(sys.argv) <= 1:
    print("No command arguments")
    exit(1)
input = sys.argv[1]
if len(sys.argv) >= 3:
    output = sys.argv[2]
else:
    output = sys.argv[1] + ".csv"
pattern = read(input)
write = write(pattern,output)
