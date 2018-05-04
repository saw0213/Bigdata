# coding: cp949
prompt = """
1. ADD
2. DEL
3. LIST
4. QUIT

Enter number: """


number = 0
while True:
    print(prompt, end='')
    number = int(input())

    if number == 4:
        break #break <- 종료되는 조건이 2개 이상일때
