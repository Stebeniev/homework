fizz = int(input("first_number"))
buzz = int(input("second_number"))
last = int(input("thirst_number"))

for a in range(1, last + 1):
    if ((a % fizz == 0) and (a % buzz == 0)):
        print('FB', end=" ")
    elif a % fizz == 0:
        print('F', end=" ")
    elif a % buzz == 0:
        print('B', end=" ")
    else:
        print(a, end=" ")



