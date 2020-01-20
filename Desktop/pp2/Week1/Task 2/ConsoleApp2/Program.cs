using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        class Student
        {
            public string name; // sozdau polya
            public int year = 0;
            public string id;
           
            public Student(string name, string id)
            {
                this.name = name;
                this.id = id;        // constructor
              // inicializiryet polya
            }

            public override string ToString()
            {
                return name + " " + id + " ";// metod
            }
            public void Incr()
            {
                year++;
                Console.WriteLine("Year of study : " + year);
            }
            

        }
        static void Main(string[] args)
        {
            Student student = new Student("Ayana", "18BD110504");
            Console.WriteLine(student);
            student.Incr();
            Console.ReadKey();
        }
    }
}
