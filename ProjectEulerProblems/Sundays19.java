
public class Sundays19 {
	public static int Sundays()
	{
		int count = 0;
		int s = 7;
		for(int y = 1900; y < 2001; y++)
		{
			for(int m = 1; m<13; m++)
			{
				int end;
				if(m==1||m==3||m==5||m==7||m==8||m==10||m==12)
				{
					end = 31;
				}
				else
				{
					if (m!= 2)
					{
						end = 30;
					}

					else
					{
					if(y%4==0&&(y%100!=0||(y%400==0)))
					{
						end=29;
					}
					else
						end = 28;
					}
				}
				for(int d=1; d <=end; d++)
				{
					if(s==d&&d==1&&y!=1900)
					{
						count++;
					}
					if(s==d)
					{
						if(s+7<=end)
						{
							s+=7;
						}
						else
						{
							int a = s;
							s = 7 -(end-a);
						}
					}
					
			    }
				
			}
					
		}
		
		
		return count;
	}

	public static void main (String [] args)
	{
		System.out.println(Sundays()); 
		
	}
}
