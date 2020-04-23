import java.util.ArrayList;

public class SumsofPowersof2andFractions 
{
	
	static int a;
	static int x;
	static int o=0;
	
	//Help with the recursion Paige....figure it out
	//Jk, didn't go the recursion route, this method generates each and every individual power
	//of two; to be placed in the next method which will generate an array of the powers 
	//of two
	public static int myMethod(int y)
	{
		x = (int)(Math.log10(y)/Math.log10(2));
		a = (int)(Math.pow(2, x));
		return a;
	}
	
	//Creates an array of LARGEST powers of two that make up the number- to be further divided
	//in the next method, countCombos, which counts all the combos of the powers of two (all of
	//the possible arrays) there are in this number
	public static ArrayList<Integer> myMethod1(int y)
	{
		ArrayList<Integer> list = new ArrayList<Integer>();
		int a = myMethod(y);
		list.add(a);
		int t = 0;
		for(int i = 0; i < list.size(); i++)
		{	t+=list.get(i);
			if(t==y)
			{
				i=list.size();
			}
			else
			{
			list.add(myMethod(y-a));
			int b = y-a;
			int c = myMethod(y-a);
			y=b;
			a=c;
			}
		}
		
		return list;
		
	}
	
	//Counts the combos of powers of two that can make up a number...stores them in an 
	//array...returns the size of the array as the number of combos...should I make this
	//a void method and then just do m.size() later on???? B/c would the recursion mess up what
	//this actually returns or nah??
	public static int countCombos (ArrayList<ArrayList<Integer>> m ,ArrayList<Integer> k)
	{	m.add(k);
		ArrayList<Integer> q = new ArrayList<Integer>(); 
		for(int i = 0; i < k.size(); i++)
		{
			if(!k.contains(k.get(i)/2))
			{
				ArrayList<Integer> t = new ArrayList <Integer>();
				t.add(k.get(i)/2);
				t.add(k.get(i)/2);
				q.addAll(k);
				q.addAll(i,t);
				q.remove(i+2);
				if(!m.contains(q))
				{countCombos(m,q);}
			}
			
		}
		return m.size();
	}
	
//Traverses all numbers to see if that and the number below it have 123456789 and 987654321 combos respectively...
//returns binary of the number to be then be counted (1s and 0s) in person
//HOWEVER, IT WILL PROBABLY BE 5 GENERATIONS BEFORE THIS PROGRAM TERMINATES
public static void main (String [] args)
{
	int i=0;
	boolean b = false;
	while (b == false)
	{
		ArrayList<ArrayList<Integer>> m = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> p = myMethod1(i-1);
		ArrayList<Integer> z = myMethod1(i);
		int c = countCombos(m,p);
		int d = countCombos(m,z);
		
		if((c == 987654321) && (d == 123456789))
		{
			System.out.println(Integer.toBinaryString(i));
			b = true;
			
		}
		
		i++;
	}
	
}
}
