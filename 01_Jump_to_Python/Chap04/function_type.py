# coding: cp949
def my_sum1(num1, num2):
    result = num1 + num2
    return result

def my_sum2(num1, num2):
    result = num1 + num2
    print("%d + %d = %d"%(num1,num2,result))

def my_sum3():
    num1 = int(input("첫번째 수를 입력하세요 : "))
    num2 = int(input("두번째 수를 입력하세요 : "))
    result = num1 + num2
    return result

def my_sum4():
    num1 = int(input("첫번째 수를 입력하세요 : "))
    num2 = int(input("두번째 수를 입력하세요 : "))
    result = num1 + num2
    print("%d + %d = %d"%(num1,num2,result))

num1 = int(input("첫번째 수를 입력하세요 : "))
num2 = int(input("두번째 수를 입력하세요 : "))
result = my_sum1(num1,num2)
print("%d + %d = %d"%(num1,num2,result))

num1 = int(input("첫번째 수를 입력하세요 : "))
num2 = int(input("두번째 수를 입력하세요 : "))
my_sum2(num1,num2)

my_sum3()
print("%d + %d = %d"%(num1,num2,result))

my_sum4()
