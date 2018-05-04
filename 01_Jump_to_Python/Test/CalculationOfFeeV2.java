import java.util.Scanner;

public class CalculationOfFeeV2{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int age = 0;
		int fee = 0;
		String grade = null;
		
		do{
			System.out.print("나이를 입력하세요 : ");
			age = sc.nextInt();
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
		}while(age<0);
	
		System.out.println("귀하는 "+grade+"등급이며 요금은 "+fee+"원 입니다.");
	sc.close();
	}
}

