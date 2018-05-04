import java.util.Scanner;

public class CalculationOfFeeV3{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int age = 0;
		int fee = 0;
		int paying = 0;
		String grade = null;
		
		do{
			System.out.print("나이를 입력하세요 : ");
			age = sc.nextInt();
			fee = age(age, fee, grade);
			
		}while(age<0);
		if(fee != 0){
			System.out.print("요금을 입력하세요 : ");
			paying = sc.nextInt();
		}
		pay(paying, fee);
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
