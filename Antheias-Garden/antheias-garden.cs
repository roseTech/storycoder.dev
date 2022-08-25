using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
        const int days = 27;
        double nOfLilies = Math.Pow(2, days - 1);
        Console.WriteLine(nOfLilies);
    }
  }
}