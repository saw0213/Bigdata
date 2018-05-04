m = int(input("Total : "))
n = int(input("Posts of page : "))

page = ((int)(m/n))
if m%n != 0:
    page = page+1
print(page)
