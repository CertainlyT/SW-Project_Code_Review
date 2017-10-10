import time
import random

def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
	if n == 0:
		return 0
	elif 0 < n <= 2:
		return 1
	elif n == 3:
		return 2
	a = 1
	b = 1
	nn = (n - 2) // 2
	for i in range(nn):
		a = a + b
		b = a + b
	if n % 2 == 0:
		return b
	else:
		a = a + b
		return a

while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
	ts = time.time()
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
