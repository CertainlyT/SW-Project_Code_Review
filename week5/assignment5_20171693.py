import time
import random

def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	oddNumber = 1
	evenNumber = 1
	nn = (n - 2) // 2
	for i in range(nn):
		oddNumber = oddNumber + evenNumber
		evenNumber = oddNumber + evenNumber
	if n % 2 == 0:
		return evenNumber
	else:
		oddNumber = oddNumber + evenNumber
		return oddNumber

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
