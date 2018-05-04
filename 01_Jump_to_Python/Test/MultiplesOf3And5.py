num = 1
count = 0
while num < 1001:
    if num%3 == 0 or num%5 == 0:
        count += num
    num = num+1
print(count)
