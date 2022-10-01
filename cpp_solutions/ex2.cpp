#include <cmath>
#include <iostream>
#include <limits>

double distance(double x1, double y1, double z1, double x2, double y2, double z2) {
    return std::sqrt( std::pow(x2 - x1, 2) + std::pow(y2 - y1, 2) + std::pow(z2 - z1, 2));
}

int main() {
    float px1, px2, py1, py2, pz1, pz2;

    std::cout << "Please enter the two points: ";
    std::cin >> px1 >> py1 >> pz1 >> px2 >> py2 >> pz2;

    std::cout.precision(std::numeric_limits<double>::digits10);
    std::cout << distance(px1, py1, pz1, px2, py2, pz2);
}
