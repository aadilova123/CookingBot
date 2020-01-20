using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string line1 = Console.ReadLine();  // schityvaet stroky 
            string line2 = Console.ReadLine();

            int n = int.Parse(line1);    // perevela string v integer
            string[] numStr = line2.Split();    // massiv razdelila probelami 

            for(int i = 0; i < numStr.Length; ++i)   // probegaus' po massivy
            {
                int x = int.Parse(numStr[i]);  // kazhdyi element perevela v type int s pomow'u Parse
                for(int a = 0; a < 2; ++a)
                {
                    Console.Write(x + ""); 
                }
                
            }
            Console.ReadKey();
        }
    }
}
