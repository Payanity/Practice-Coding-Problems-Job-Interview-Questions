import java.util.Scanner;

public class flower {

	public static void main (String[]arg)
	{
		   System.out.println("Please enter the query  :");
		    Scanner scan2 = new Scanner(System.in);
		    String word2 = scan2.nextLine();
		    String[] array2 = word2.split(" ");
		    System.out.println(word2);
		    
		    boolean b = true;
		    for (int i = 1; i < array2.length; i++)
		    {
		    	
		    	String y = array2[i];
		    	String x = array2[i-1];
		    
		    	if(x.charAt(0)!= y.charAt(0))
		    	{
		    		b = false;
		    	}
		    }    
		    if(b==true)
		    	System.out.println('Y');
		    else
		    	System.out.println('N');
	}
}
