sum = 10500
bancnote = [1000, 500, 200, 100]
for x in list(bancnote):
    bancnote = sum // x
    sum -= bancnote * x
    print(x)