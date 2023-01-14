 using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SoloLearn
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                int drinks = Convert.ToInt32(Console.ReadLine());
                int shelves = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine(drinks / shelves);

            }
            
            catch (DivideByZeroException ze)
            {
                Console.WriteLine("At least 1 shelf");
            }
            catch(FormatException fe) 
            {
                Console.WriteLine("Please insert an integer");
            }
        }
    }
}