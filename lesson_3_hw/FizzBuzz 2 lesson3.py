import sys
filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
	fizz, buzz, last = [int(element) for element in line.split('\n')[0].split(' ')]
	print(fizz, buzz, last)
	for i in range(1, last + 1):
		if i % fizz == 0 and i % buzz == 0:
			print('FB', end=" ")
		elif i % fizz == 0:
			print('F', end=" ")
		elif i % buzz == 0:
			print('B', end=" ")
		else:
			print(i, end=" ")
	print()
f.close()




