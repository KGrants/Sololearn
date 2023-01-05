using System; 

namespace Sololearn
{
	class Program
	{
		public static void Main(string[] args)
		{
			const double pi = 3.14;
			double radius = Convert.ToDouble(Console.ReadLine());
			double area = pi*(radius*radius);
			Console.WriteLine(area);
		}
	}
}