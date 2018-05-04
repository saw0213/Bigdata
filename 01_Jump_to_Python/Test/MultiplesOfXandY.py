# coding: cp949

while True:
    x = int(input("x : "))
    y = int(input("y : "))
    z = int(input("z : "))

    if z <= 0:
        break;

    for i in range(1,z+1):
        if i%x == 0 and i%y == 0:
            print(i)
