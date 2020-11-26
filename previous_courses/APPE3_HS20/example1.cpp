#include <iostream>

void compare(int x, int y) {
    if (x > y) {
        std::cout << 1 << '\n';
    } else if (x < y) {
        std::cout << -1 << '\n';
    } else {
        std::cout << 0 << '\n';
    }
}