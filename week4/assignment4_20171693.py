
def Combination(n, m):
    if n == 0 or m == 0:
        return 0
    if n == m:
        return 1
    elif m == 1:
        return n
    else:
        return Combination(n - 1, m) + Combination(n - 1, m - 1)
n=0
m=0
while True:
    n = int(input("Enter n:"))
    m = int(input("Enter m:"))
    if n == -1:
        break
    elif m > n:
        print("ERROR")
        continue
    print("C(%d,%d) =" %(n, m),Combination(n, m))
