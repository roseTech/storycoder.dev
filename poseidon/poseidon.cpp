#include <iostream>
#include <iomanip>

int main()
{
    double tempSeidon = 11.475 + 14.0;
    double tempCelsius = tempSeidon / 1.37;
    std::cout << std::setprecision(2) << std::fixed;
    std::cout << tempCelsius << std::endl;
    return 0;
}
