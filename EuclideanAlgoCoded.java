import java.util.Scanner;
public class EucAlgo {

	public static void main(String [] args)
	{
		System.out.println("Enter an integer.");
		Scanner scan = new Scanner(System.in);
		int i = scan.nextInt();
		System.out.println("Enter another integer.");
		int j = scan.nextInt();
		
		int a;
		
		while(i!=j)
		{
			if(i>j)
			{   
				a=j;
				j=i-j;
				i=a;
				
			}
			else
			{
				a=i;
				i=j-i;
				j=a;
			}
		}
		
		System.out.println("The greatest common denominator is " + j);
		
	}
}
