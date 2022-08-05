import sys
filename = sys.argv[1]
f = open(filename, 'r')
d = f.read()
list = d.split(' ')
a = list[::-1]
print(a)
f.close()

