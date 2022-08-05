import sys
filename = sys.argv[1]
filename1 = 'FizzBuzz3'
f = open(filename, 'r')
d = open(filename1, 'w')
for line in f:
	fizz, buzz, last = [int(element) for element in line.split('\n')[0].split(' ')]
	print(fizz, buzz, last)
	for i in range(1, last + 1):
		if i % fizz == 0 and i % buzz == 0:
			d.write('FB ')
		elif i % fizz == 0:
			d.write('F ')
		elif i % buzz == 0:
			d.write('B ')
		else:
			d.write(str(i) + ' ')
	d.write('\n')
f.close()
d.close()




