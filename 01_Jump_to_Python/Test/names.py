# coding: cp949

names = '������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������'.split(',')

""" 1. �达�� �̾��� ���� �� �� �ΰ���? """

count_k = 0
count_l = 0

for i in names:
    if i[0] == '��':
        count_k = count_k+1
    if i[0] == '��':
        count_l = count_l+1
print("�达 : " +str(count_k)+"   �̾� : "+str(count_l))

""" 2. "���翵"�̶� �̸��� �� �� �ݺ��ǳ���? """

count_ljy = 0

for i in names:
    if i == '���翵':
        count_ljy = count_ljy+1
print("���翵�� �� : " +str(count_ljy))


""" 3. �ߺ��� ������ �̸��� ����ϼ��� """

print(set(names))

"""" 4. �ߺ��� ������ �̸��� ������������ �����Ͽ� ����ϼ��� """

list_names = list(set(names))
list_names.sort()
print(list_names)
