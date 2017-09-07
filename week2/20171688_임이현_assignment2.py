while(1):
    n = int(input())
    if n==-1:
        break

    res = 1
    for i in range(1, n+1):
        res *= i

    print(res)