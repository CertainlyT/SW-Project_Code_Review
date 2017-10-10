import time

def iterfibo(nbr):
    sum = 0
    before = 0
    after = 1

    if nbr > 2:
        for i in range(nbr-1):
            sum = before + after
            before = after
            after = sum

    return sum

def fibo(nbr):
    if nbr == 0:
        return 0
    elif nbr == 1:
        return 1
    else:
        return fibo(nbr - 1) + fibo(nbr - 2)


while True:
    nbr = int(input("Enter a number: "))

    if nbr == -1:
        break

    ts = time.time()
    fibonumber = iterfibo(nbr)

    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))

    ts = time.time()
    fibonumber = fibo(nbr)

    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
    pass