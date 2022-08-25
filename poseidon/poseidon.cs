using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
        float tempSeidon = 25.475f;
        float tempCelsius = (tempSeidon / 1.37f);
        Console.WriteLine(String.Format("{0:0.##}", tempCelsius));
    }
  }
}