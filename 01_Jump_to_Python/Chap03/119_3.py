#coding: cp949
A=True
B=False

if A==False and B==False:
    print("A==False and B==False 조건이어야 수행되는 명령문")

if A and B == False:
    print("""A==False and B==False 조건이어야 수행하는 의도이면
    현재 A는 True인데도 print가 되므로 조건식이 잘못 작성됨""")
