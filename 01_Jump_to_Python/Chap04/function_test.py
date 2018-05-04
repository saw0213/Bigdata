def cal(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = args[0]
        for i in args[1:]:
            result = result * i

    elif choice == "min":
        result = 0
        for i in args:
            result = result - i

    elif choice == "div":
        result = args[0]
        for i in args[1:]:
            result = result / i
    return result

choice = input(":")
result = cal(choice, 10,5,1)
print(result)
