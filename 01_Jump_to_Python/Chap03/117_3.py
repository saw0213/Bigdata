# coding: cp949
money = int(input("�󸶸� ������ �ֽ��ϱ�? : "))
#card = 1 <- ī�� ���� ���θ� �Ǵ��ϹǷ� �������� �޸� ���� ����
#card = True
card = input("ī�带 �����ϰ� �ֽ��ϱ�? (y/n) : ")
if card == 'y':     card = True
else:               card = False

if money >= 3000:
    print("�ýø� Ÿ�� ����")
else:
    if card == True:
        #print("�ýø� Ÿ����") #������ �ڵ��� ��� �ߺ�������
        print("ī�� �ýø� Ÿ����") #�������� ���� �ڵ��� ��� �ߺ�����
  
  print("�ɾ��")

