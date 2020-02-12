#include <sol/sol.hpp>
#include <cassert>
#include <iostream>

int main() {
    sol::state lua;
    int x = 0;
    lua.set_function("beep", [&x]{ ++x; });
    lua.script("beep()");
    
    if(x == 1)
    {
        std::cout << "Passed\n";
        return 0;
    }
    else
    {
        std::cout << "Failed\n";
        return 1;
    }
}