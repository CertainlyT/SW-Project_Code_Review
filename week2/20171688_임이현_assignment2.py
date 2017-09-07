# while문이 일정 조건일 때만 돌아가도록 코드를 수정했다_2번째 코드
print("숫자를 입력해주세요. -1을 입력할 경우 프로그램이 종료됩니다.")
n = int(input(숫자를 입력해주세요 :))
while(n!=-1):
    res = 1
    for i in range(1, n+1):
        res *= i
    print(res)
    n = int(input(숫자를 입력해주세요 :)) #새로운 숫자를 또 받기 위해 while문 마지막에 입력을 또 받는다
