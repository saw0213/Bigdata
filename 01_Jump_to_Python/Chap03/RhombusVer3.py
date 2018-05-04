# coding: cp949
num = 1
while True:
    while True:
        num = (int)(input("홀수 입력(0은 종료) : "))
        if num%2 == 1:
            break
        elif num == 0:
            break
        else:
            print("%d는 짝수입니다."%num)

    if num == 0:
        print("프로그램을 종료합니다.")
        break

    line = 0
    star = 1
    space = (int)((num+1)/2-1)  #기본 한칸 출력이라 끝에 -1

    print(" " + "-"*num)
    while line < num:
        print("|" + " "*space + "*"*star + " "*space+"|")
        if line < (num-1)/2:
            space = space-1
            star = star+2
        else:
            space = space+1
            star = star-2
        line = line+1
    print(" " + "-"*num)
