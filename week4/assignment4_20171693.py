
def Combination(n, m):
    if n == 0 or m == 0:
        return 0
    elif n < -1 or m < -1:
        return 0
    elif n == m:
        return 1
    elif m == 1:
        return n
    else:
        return Combination(n - 1, m) + Combination(n - 1, m - 1)
n = 0
m = 0
while True:
    try:
        n = int(input("Enter n:"))      # n 또는 m 이 -1일 시 무조건 그 순간 break 처리
        if n == -1:
            break
        m = int(input("Enter m:"))
        if m == -1:
            break
        if m < -1 or n < -1:
            print("C(%d,%d) =" % (n, m), Combination(n, m)) #음수일 시 return 0으로 처리해주기 위함(m > n 아닐 경우를 위해
        else:
            if m > n:
                print("ERROR")
                continue
            print("C(%d,%d) =" % (n, m), Combination(n, m))
    except:
        print("VALUE ERROR")
