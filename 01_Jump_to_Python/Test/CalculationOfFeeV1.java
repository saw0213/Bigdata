import java.util.Scanner;

public class CalculationOfFeeV1{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		System.out.print("���̸� �Է��ϼ��� : ");
		int age = sc.nextInt();
		int fee = 0;

		if((age>=0 && age<=3) || age>=66) {fee = 0;} 
		else if(age>=4 && age<=13){fee = 2000;}
		else if(age>=14 && age<=18){fee = 3000;}
		else if(age>=19 && age<=65){fee = 5000;}

		System.out.println("����� "+fee+"�� �Դϴ�.");
		sc.close();
	}
}

