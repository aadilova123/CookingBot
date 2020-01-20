using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    class Program
    {
        static void Main(string[] args)
        {
            string n = Console.ReadLine();
            int x = int.Parse(n);
            string[,] a = new string[x, x];

            for (int i = 0; i < x; i++)
                for (int j = 0; j < i + 1; j++)
                    a[i, j] = "*";

            for (int i = 0; i < x; i++)
            {
                for (int j = 0; j < i + 1; j++)
                    Console.Write(a[i, j] + " ");
                Console.WriteLine();
            }
        }
    }
}