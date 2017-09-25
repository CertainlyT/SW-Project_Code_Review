def facto(n):
    f = 1
    for i in range (1,n+1) :
        f *= i
    return f

def combination(n, m):
    return int(facto(n) / (facto(m) * facto(n - m)))

def calculate(n, m):
    if (m == 0 or n==m):
        return 1
    elif n < m:
        return 0
    else:
         return combination(n - 1, m) + combination(n - 1, m - 1)


n = int(input("Enter n:"))
m = int(input("Enter m: "))
print( calculate(n, m))