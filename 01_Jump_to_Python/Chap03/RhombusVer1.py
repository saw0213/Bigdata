# coding: cp949
num = 1
while True:
    while True:
        num = (int)(input("Ȧ�� �Է�(0�� ����) : "))
        if num%2 == 1:
            break
        elif num == 0:
            break
        else:
            print("%d�� ¦���Դϴ�."%num)

    if num == 0:
        print("���α׷��� �����մϴ�.")
        break
    
    line = 0
    star = 1
    space = (int)((num+1)/2-1) #�⺻ ��ĭ ����̶� ���� -1

    while line < (num+1)/2:
        print(" "*space + "*"*star)
        space = space-1
        star = star+2
        line = line+1
