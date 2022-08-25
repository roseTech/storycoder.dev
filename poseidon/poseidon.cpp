#include <iostream>
#include <iomanip>

int main()
{
    double tempSeidon = 25.475;
    double tempCelsius = tempSeidon / 1.37;
    std::cout << std::setprecision(2) << std::fixed;
    std::cout << tempCelsius << std::endl;
    return 0;
}
