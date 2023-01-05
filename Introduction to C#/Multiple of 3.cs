using System; 
using System.Collections.Generic;

namespace Sololearn
{
	class Program
	{
		public static void Main(string[] args)
		{
			int number = int.Parse(Console.ReadLine());
			
			for (int i = 1; i <= number; i++)
			{
				if (i%3==0)
					Console.Write("*");
				else
					Console.Write(i);
            	}
		}
	}
}