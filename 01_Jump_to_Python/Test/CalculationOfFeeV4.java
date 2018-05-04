import java.util.Scanner;

public class CalculationOfFeeV4{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int age = 0;			//나이
		double fee = 0;			//요금
		int paying = 0;			//지불금액
		int payingWay = 0;		//지불방법
		String grade = null;	//등급
		
		do{
			System.out.print("나이를 입력하세요 : ");
			age = sc.nextInt();
			fee = age(age, (int)fee, grade);

		}while(age<0);
		
		do{
			if(fee == 0){
				pay(paying, (int)fee);
				break;
			}

			System.out.print("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용카드) : ");
			payingWay = sc.nextInt();

			if(payingWay == 1){
				System.out.print("요금을 입력하세요 : ");
				paying = sc.nextInt();
				pay(paying, (int)fee);
				break;

			}else if(payingWay == 2){
				fee = fee*0.9;
				if(age>=60&&age<=65){fee = fee*0.95;}
				System.out.println((int)fee+"원 결제 되었습니다. 티켓을 발행합니다.");
				break;

			}else{
				System.out.println("잘못된 입력입니다.");

			}

		}while(true); 


		sc.close();
	}
	
	public static int age(int age,int fee, String grade){
			if((age>=0 && age<=3) || age>=66) {
				fee = 0;
				if(age<4){grade="유아";}
				else{grade="노인";}

			} else if(age>=4 && age<=13){
				fee = 2000;
				grade="어린이";

			}else if(age>=14 && age<=18){
				fee = 3000;
				grade="청소년";

			}else if(age>=19 && age<=65){
				fee = 5000;
				grade="성인";

			}else{
				System.out.println("다시 입력하세요");

			}

			if(age>=0){	System.out.println("귀하는 "+grade+"등급이며 요금은 "+fee+"원 입니다.");}
		return fee;
	}

	public static void pay(int paying, int fee){
		if(paying<fee){
			System.out.println((fee-paying)+"가 모자랍니다. 입력하신"+paying+"를 반환합니다.");

		}else if(paying>fee){
			System.out.println("감사합니다. 티켓을 발행하고 거스름돈 "+(paying-fee)+"를 반환합니다.");

		}else{
			System.out.println("감사합니다. 티켓을 발행합니다.");

		}
	}

}
