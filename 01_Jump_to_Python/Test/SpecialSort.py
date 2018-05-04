number = [-1, 1, 3, -2, 2]
minus= []
plus = []

for i in number:
    if i < 0 :
        minus.append(i)
    elif i > 0:
        plus.append(i)

print (minus + plus)

