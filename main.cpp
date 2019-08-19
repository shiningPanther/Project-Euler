#include "Problem67.hpp"
#include <iostream>


int main() {
    // Note on measurement of elapsed time:
    // clock() returns the number of clock ticks at the time when called. For the variable 'duration', the number of clock ticks for running the function are then determined. The constant CLOCKS_PER_SEC specifies how many clock ticks there are within a second, returning the elapsed time in s.
    std::clock_t start;
    double duration;
    start = std::clock();
    
    // Solution to the problem
    long solution = Problem67();
    
    duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
    std::cout << "Program finished in: " << duration << " s \n";
    std::cout << "Solution: " << solution << "\n";
    return 0;
}
