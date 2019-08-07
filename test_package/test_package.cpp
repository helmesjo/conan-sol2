#include <sol/sol.hpp>
#include <cassert>
#include <iostream>

int main() {
    sol::state lua;
    int x = 0;
    lua.set_function("beep", [&x]{ ++x; });
    lua.script("beep()");
    assert(x == 1);
    std::cout << "Passed\n";
}