#Продолжаем идеализировать fizzbuzz, теперь применяем функции и map везде, где можно и нельзя!
import sys
filename = sys.argv[1]
f = open(filename, 'r')
def fun2(i, fizz, buzz):
	if not i % fizz and not i % buzz:
		return 'FB'
	elif not i % fizz:
		return 'F'
	elif not i % buzz:
		return 'B'
	else:
		return str(i)

def fun1(line):
	fizz, buzz, last = [int(element) for element in line.split('\n')[0].split(' ')]
	print(fizz, buzz, last)
	res = list(map(fun2, range(1, last + 1), [fizz]*last, [buzz]*last))
	print(" ".join(res))

def main():
	for line in f:
		fun1(line)

main()
print()
f.close()