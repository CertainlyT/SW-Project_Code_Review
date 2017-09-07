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

    if num == 0:
        print(str(num) + "! = " + "1")
    else:
        for value in range(1, num + 1):
            result *= value
        print(str(num) + "! = " + str(result))
