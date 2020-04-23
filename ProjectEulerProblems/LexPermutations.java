import java.util.ArrayList;

public class LexPermutations 
{
	
	public static String lexPerm()
	{
		String a;
		String b;
		String c;
		String d;
		String e;
		String f;
		String g;
		String h;
		String i;
		String j;
		ArrayList<String> perm = new ArrayList<String>();
		/*Nested forLoops; the x's signify a repetition in the permutations;
		 * for Loops do add permutation to arrayList with x's there; prints out 
		 * String.
		 */
		for(int k = 0; k <=9; k++)
		{
			a = Integer.toString(k);
			
			for(int l = 0; l<=9; l++)
			{
				if(l!=k)
				{
					b = Integer.toString(l);
				}
				else
				{
					b = "x";
				}
				
			    for(int m = 0; m <=9; m++)
			    {
			    	if(m!=k||m!=l)
			    	{
			    		 c = Integer.toString(m);
					}
					else
					{
						c = "x";
					}
			    	
			    	for(int n = 0; n <=9; n++)
				    {
				    	if(n!=k||n!=l||n!=m)
				    	{
				    		d = Integer.toString(n);
						}
						else
						{
							d = "x";
						}
				    	
				    	for(int o = 0; o <=9; o++)
					    {
					    	if(o!=k||o!=l||o!=m||o!=n)
					    	{
					    	   e = Integer.toString(o);
							}
							else
							{
								e = "x";
							}
					    	
					    	for(int p = 0; p<=9; p++)
					    	{
					    		if(p!=k||p!=l||p!=m||p!=n||p!=o)
						    	{
						    	    f = Integer.toString(p);
								}
								else
								{
								    f = "x";
								}
						    	
					    		for(int q = 0; q<=9; q++)
						    	{
						    		if(q!=k||q!=l||q!=m||q!=n||q!=o||q!=p)
							    	{
							    		g = Integer.toString(q);
									}
									else
									{
										g = "x";
									}
							    	
						    		for(int r = 0; r<=9; r++)
							    	{
							    		if(r!=k||r!=l||r!=m|r!=n||r!=o||r!=p||r!=q)
								    	{
								    		h = Integer.toString(r);
										}
										else
										{
											h = "x";
										}
							    		
							    		for(int s = 0; s<=9; s++)
								    	{
								    		if(s!=k||s!=l||s!=m|s!=n||s!=o||s!=p||s!=q||s!=r)
									    	{
									    		i = Integer.toString(s);
											}
											else
											{
												i = "x";
											}
								    		
								    		for(int t = 0; t<=9; t++)
									    	{
									    		if(t!=k||t!=l||t!=m|t!=n||t!=o||t!=p||t!=q||t!=r||t!=s)
										    	{
										    		j = Integer.toString(t);
												}
												else
												{
													j = "x";
												}
									    	
									    		if (!((a+b+c+d+e+f+g+h+i+j).contains("x")))
									    		{
									    			perm.add(a+b+c+d+e+f+g+h+i+j);
									    		}
									    	}
								    	}
							    	
							    	}
						    	}
					    	}
				    	
					    }
				    }
			    }
			}
		}
	
		return perm.get(999999);
	}

	public static void main (String [] args)
	{
		lexPerm();
	}
}