# coding: cp949

prompt="""
1. Ŀ�� ����
2. Ŀ�� �ܷ� Ȯ��
3. ���α׷� ���� """

coffee = 10

while coffee > 0:
    print(prompt)
    number = int(input("�޴��� �����ϼ��� : "))

    if number == 1:
        money = int(input("���� �־��ּ��� : "))
        if money == 300:
            print("Ŀ�Ǹ� �ݴϴ�.")
            coffee = coffee -1
        elif money > 300:
            print("�Ž����� %d���� Ŀ�Ǹ� �ݴϴ�." %(money-300))
            coffee = coffee -1
        elif money < 300 and money > -1:
            print("%d���� ������ Ŀ�Ǹ� ���� �ʽ��ϴ�."%(300-money))
        else:
            print("�߸��� ���� �Է��Դϴ�.")

        if coffee == 0:
            print("��� Ŀ�ǰ� ���� �Ǿ� ���α׷��� �����մϴ�.")

    elif number == 2:
        print("���� Ŀ�Ǵ� %d ���Դϴ�." %coffee)
    
    elif number == 3:
        print("���α׷��� �����մϴ�.")
        break
    else:
        print("�߸��� ���� �Է��Դϴ�.")
