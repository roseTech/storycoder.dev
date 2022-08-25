#include <cstdio>
#include <iostream>
#include <iomanip>

int main()
{
    float tempSeidon = 25.475;
    float tempCelsius = (tempSeidon / 1.37f);
    std::cout << std::setprecision(2) << std::fixed;
    std::cout << tempCelsius;

    return 0;
}