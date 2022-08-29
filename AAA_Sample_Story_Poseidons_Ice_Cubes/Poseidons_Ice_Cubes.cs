using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
        double tempSeidon = 11.475 + 14.0;
        double tempCelsius = tempSeidon / 1.37;
        Console.WriteLine(String.Format("{0:0.##}", tempCelsius));
    }
  }
}
