using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Task1_lab1
{
    class Program
    {
        public static bool Prime(int n)
        {
            for (int i = 2; i * i <= n; i++)
            {
                if (n % i == 0) return false;
            }
            return true;
        }


        static void Main(string[] args)
        {
            string line1 = Console.ReadLine(); // schityvau stroki 
            string line2 = Console.ReadLine();

            int n = int.Parse(line1);  // 1 stroky perevela v tip integer
            string[] s = line2.Split(); // sozdau massiv s , tam razdelila 2 stroky cherez probely
            List<int> vs = new List<int>(); // sozdala novyi list iz intov
            List<int> vs1 = new List<int>();
            for (int i = 0; i < s.Length; ++i)
            {
                int x = int.Parse(s[i]);  // perevratila kazhdyi element massiva v int
                vs.Add(x);
            }// pomestila vse elementy v list intov
                for (int k = 0; k < vs.Count; ++k)
                {
                    // probegayus' i proverayu elementy na is prime or not
                    if (Prime(vs[k]) == true && vs[k] != 1)
                    {
                        vs1.Add(vs[k]);
                    }  
                }
            Console.WriteLine(vs1.Count);
            for (int m = 0; m < vs1.Count; m++)
            {
                Console.Write(vs1[m]+ " ");
            }
        }
    }
}
