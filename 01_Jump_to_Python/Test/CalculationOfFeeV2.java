import java.util.Scanner;

public class CalculationOfFeeV2{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int age = 0;
		int fee = 0;
		String grade = null;
		
		do{
			System.out.print("���̸� �Է��ϼ��� : ");
			age = sc.nextInt();
			if((age>=0 && age<=3) || age>=66) {
				fee = 0;
				if(age<4){grade="����";}
				else{grade="����";}
			} else if(age>=4 && age<=13){
				fee = 2000;
				grade="���";
			}else if(age>=14 && age<=18){
				fee = 3000;
				grade="û�ҳ�";
			}else if(age>=19 && age<=65){
				fee = 5000;
				grade="����";
			}else{
				System.out.println("�ٽ� �Է��ϼ���");
			}
		}while(age<0);
	
		System.out.println("���ϴ� "+grade+"����̸� ����� "+fee+"�� �Դϴ�.");
	sc.close();
	}
}

