#  *fectorial

# def facto(n):
#     f = 1
#     for i in range (1,n+1) :
#         f *= i
#     return f
#
# def combination(n, m):
#     return int(facto(n) / (facto(m) * facto(n - m)))

def calculate(n, m):
    if (m == 0 or n==m):
        return 1
    elif n < m:
        return 0
    else:
         return calculate(n - 1, m) + calculate(n - 1, m - 1)


while (1):
    try:
        n = int(input("Enter n:"))
        m = int(input("Enter m: "))
        if n == -1:
            break
        elif n<=0 or m< 0 :
            print(" \tn>0이어야 하고 m>=0 이어야 합니다.\n\t값을 다시 입력해주세요.")
            continue
        elif n>0 or m>=0:
            break

    except ValueError:
        print("값을 입력해주세요.")


    print( calculate(n, m))