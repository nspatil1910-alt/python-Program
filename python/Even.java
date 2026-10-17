/*Java Program to Check Whether a Given Number is Even or Odd*/
import java.util.Scanner;
public class 
{
	public static void main(String[] args)
	{
		int n;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a Number");
		int n =sc.nextInt();
		if(n%2==0)
		{
			System.out.println("Number is Even");
		}
		else
		{
			System.out.println("Number is odd");
		}
	}
}
