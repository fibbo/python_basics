#include <iostream>

template<typename T>
void compare(T x, T y) {
    if (x > y) std::cout << 1 << '\n';
    else if (x < y) std::cout << -1 << '\n';
    else std::cout << 0 << '\n';
}

int main() {
    int a, b;
    std::cout << "Please enter a and b for comparison\n";
    std::cin >> a >> b;
    compare(a, b);
}