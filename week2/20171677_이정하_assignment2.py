# factorial

# do-while loop
# while True:
#     work()
#     if "condition":
#         break

# 무한 loop
while True:
    result = 1
    num = int(input("Enter a number: "))
    if num == -1:
        break
    elif num == 0:
        print(str(num) + "! = " + "1")
    elif num < 0:
        print()
    else:
        for value in range(1, num + 1):
            result *= value
        print("%d != " %num, result)