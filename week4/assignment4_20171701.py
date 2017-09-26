def combination(n, r):
    if r == 0:
        return 1
    elif n == r:
        return 1
    elif n < r:
        return 0
    else:
        return combination(n-1, r) + combination(n-1, r - 1)


def factorial(n):
    facto = 1
    for i in range(n, 0, -1):
        facto *= i
    return facto


def combinationf(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


while True:
    try:
        n = int(input("Enter n: "))
        r = int(input("Enter r: "))

        if n == -1 or r == -1:
            break
        elif n < 0 or r < 0:
            print("양수를 입력하세요")
        elif n < r:
            print("성립하지 않는 조건입니다")
        else:
                print("C(%d, %d): %d" % (n, r, combination(n, r)), "Using recursive function")
                print("C(%d, %d): %d" % (n, r, combinationf(n, r)), "Using factorial")
    except ValueError:
        print("숫자를 입력해주세요")