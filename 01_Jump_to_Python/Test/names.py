# coding: cp949

names = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'.split(',')

""" 1. 김씨와 이씨는 각각 몇 명 인가요? """

count_k = 0
count_l = 0

for i in names:
    if i[0] == '김':
        count_k = count_k+1
    if i[0] == '이':
        count_l = count_l+1
print("김씨 : " +str(count_k)+"   이씨 : "+str(count_l))

""" 2. "이재영"이란 이름이 몇 번 반복되나요? """

count_ljy = 0

for i in names:
    if i == '이재영':
        count_ljy = count_ljy+1
print("이재영의 수 : " +str(count_ljy))


""" 3. 중복을 제거한 이름을 출력하세요 """

print(set(names))

"""" 4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요 """

list_names = list(set(names))
list_names.sort()
print(list_names)
