n = int(input())
while n != -1:
    fact = 1
    if n <= -2:
        print("Not identified")
        n = int(input())
    else:
        for i in range(1, n + 1):
            fact *= i
        print("%d! =" % n, fact)
        n = int(input())
