import java.util.Scanner;

public class CalculationOfFeeV5{
	//Ƽ�� ��������
	static int freeTicket = 3;		//����Ƽ�� 3��
	static int discountTicket = 5;	//����Ƽ�� 5��

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int age = 0;			//����
		double fee = 0;			//���
		int paying = 0;			//���ұݾ�
		int payingWay = 0;		//���ҹ��
		int count = 0;			//�̺�Ʈ ī��Ʈ
		String grade = null;	//���
		
		do{
			do{
				System.out.print("���̸� �Է��ϼ��� : ");
				age = sc.nextInt();
				fee = age(age, (int)fee, grade);

			}while(age<0);
		
			do{
				if(fee == 0){
					count = pay(paying, (int)fee, count);
					break;
				}
				System.out.print("��� ������ �����ϼ���. (1: ����, 2: ���� ���� �ſ�ī��) : ");
				payingWay = sc.nextInt();

				if(payingWay == 1){
					System.out.print("����� �Է��ϼ��� : ");
					paying = sc.nextInt();
					count = pay(paying, (int)fee, count);
					break;

				}else if(payingWay == 2){
					fee = fee*0.9;
					if(age>=60&&age<=65){fee = fee*0.95;}
					System.out.println((int)fee+"�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�.");
					count++;
					break;

				}else{
					System.out.println("�߸��� �Է��Դϴ�.");
				}

			}while(true); 

			giveTickets(count);
			System.out.println();
		}while(true);
	}
	
	public static int age(int age,int fee, String grade){
			if((age>=0 && age<=3) || age>=66) {
				fee = 0;
				if(age<4){grade="����";}
				else{grade="����";}

			}else if(age>=4 && age<=13){
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

			if(age>=0){	System.out.println("���ϴ� "+grade+"����̸� ����� "+fee+"�� �Դϴ�.");}
		return fee;
	}

	public static int pay(int paying, int fee, int count){
		if(paying<fee){
			System.out.println((fee-paying)+"�� ���ڶ��ϴ�. �Է��Ͻ�"+paying+"�� ��ȯ�մϴ�.");
			count--;

		}else if(paying>fee){
			System.out.println("�����մϴ�. Ƽ���� �����ϰ� �Ž����� "+(paying-fee)+"�� ��ȯ�մϴ�.");

		}else{
			System.out.println("�����մϴ�. Ƽ���� �����մϴ�.");
			if(fee == 0){count--;}

		}
		return ++count;
	}

	public static void giveTickets(int count){
		if(count != 0 && count%7==0 && freeTicket != 0){
			freeTicket--;
			System.out.println("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� : "+freeTicket);
		}
		if(count != 0 && count%4==0 && discountTicket != 0){
			discountTicket--;
			System.out.println("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� : "+discountTicket);			
		}
	}

}
