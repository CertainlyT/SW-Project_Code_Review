import time


def recurfibo(n):
    if n <= 1:
        return n
    return recurfibo(n-1) + recurfibo(n-2)


def iterfibo(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-2] + fibo[i-1])
    return fibo[n]


n = int(input("Enter a number: "))

while n != -1:
    start = time.time()
    num = iterfibo(n)
    end = time.time()
    print("iterfibo(%d)=%d, time %.6f" % (n, num, end - start))
    start = time.time()
    num = recurfibo(n)
    end = time.time()
    print("recurfibo(%d)=%d, time %.6f" % (n, num, end - start))
    n = int(input("Enter a number: "))
