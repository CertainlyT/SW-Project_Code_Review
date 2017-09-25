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


n = int(input("Enter n: "))
r = int(input("Enter r: "))

if n < 0 or r < 0:
    print("양수를 입력하세요")
else:
    print("C(n, r):", combination(n, r))
    print("C(n, r):", combinationf(n, r))