# coding: cp949

prompt="""
1. 커피 구매
2. 커피 잔량 확인
3. 프로그램 종료 """

coffee = 10

while coffee > 0:
    print(prompt)
    number = int(input("메뉴를 선택하세요 : "))

    if number == 1:
        money = int(input("돈을 넣어주세요 : "))
        if money == 300:
            print("커피를 줍니다.")
            coffee = coffee -1
        elif money > 300:
            print("거스름돈 %d원과 커피를 줍니다." %(money-300))
            coffee = coffee -1
        elif money < 300 and money > -1:
            print("%d원이 부족해 커피를 주지 않습니다."%(300-money))
        else:
            print("잘못된 숫자 입력입니다.")

        if coffee == 0:
            print("모든 커피가 소진 되어 프로그램을 종료합니다.")

    elif number == 2:
        print("남은 커피는 %d 잔입니다." %coffee)
    
    elif number == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 숫자 입력입니다.")
