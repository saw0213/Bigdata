# coding: cp949
card = input("ī�带 �����ϰ� �ֽ��ϱ�? (y/n) : ")
partnership = input("��Ű��ó �ý� �����Դϱ�? (y/n)")
if card == 'y':
    card = True
else:
    card = False

if partnership == 'y':
    partnership = True
else:
    partnership = False

#if card == True:
#   if partnership == True:
#       print("�ýø� Ÿ�� ���� �� �ֽ��ϴ�.")  <-�ڵ��ߺ�
if card == True and partnership == True:
    print("�ýø� Ÿ�� ���� �� �ֽ��ϴ�.")
#if card and partnership == True: <- ������ �������� �ؾ���
else:
    print("�ɾ�ž� �մϴ�.")
