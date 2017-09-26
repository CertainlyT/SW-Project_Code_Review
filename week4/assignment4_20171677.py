# 20171677 이정하
# assignment4 :조합으로 factorial 만들기

def combination_recursive(n, r):
    if n == 0 or r == 0:
        return 1
    elif n < r or n < 0 or r < 0:
        return 0
    elif n == r:
        return 1
    else:
        return combination_recursive(n-1, r) + combination_recursive(n-1, r-1)


while True:
    try:
        n = int(input("Enter n : "))

        if n == -1:
            break
        m = int(input("Enter m : "))

    except ValueError:
        print("숫자를 입력해주세요")
        continue

    print("C(%d,%d) = %d" %(n, m, combination_recursive(n, m)))



