# coding: cp949
money = int(input("�󸶸� ������ �ֽ��ϱ�? : "))
#card = 1 <- ī�� ���� ���θ� �Ǵ��ϹǷ� �������� �޸� ���� ����
#card = True
card = input("ī�带 �����ϰ� �ֽ��ϱ�? (y/n) : ")
if card == 'y':
    card = True
else:
    card = False

if money >= 3000 or card:
    print("�ýø� Ÿ�� ����")
else:
    print("�ɾ��")