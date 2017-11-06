#While True문을 지양하고 조건while문을 활용하기 위해 첫 번째 값만 미리 받아준다.
F_Number=int(input("Enter a number: "))
#입력받는 F_Number의 값이 -1이 될 때 까지 while문을 통해 반복해준다.
while F_Number!=-1 :
    if F_Number >=0:
        output = 1               #변수 초기화
        for i in range(1, F_Number+1):
            output *= i          #for 문을 통해 팩토리얼 구현
        print("%d! =" %F_Number, output)          #팩토리얼 값 출력
    F_Number = int(input("Enter a number: "))           #1번 줄에서 F_Number를 받았기 때문에 while의 마지막에서 입력을 받아야 함.
