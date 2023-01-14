using System;
using System.Collections.Generic;

namespace Code_Coach_Challenge
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = {
                "home",
                "programming",
                "victory",
                "C#",
                "football",
                "sport",
                "book",
                "learn",
                "dream",
                "fun"
            };

            string letter = Console.ReadLine();

            int count = 0;
            
            for (int i = 0; i<words.Length; i++)
            {
                if(words[i].Contains(letter))
                {
                    count++;
                    Console.WriteLine(words[i]);
                }
            }
            
            
            if (count == 0)
            Console.WriteLine("No match");
        }
    }
}