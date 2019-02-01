/*
 A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 
 a^2 + b^2 = c^2
 For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
 
 There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 Find the product abc.
 */


#include "Problem9.h"
#include <iostream>
using namespace std;

int Problem9() {
    int result = 0;
    int aMax = 300;
    int bMax = 500;
    // Just loop all the numbers, assuming that a is always smaller than b
    for (int a = 1, bMin = 2; a < aMax; a++, bMin++) {
        for (int b = bMin; b < bMax; b++) {
            int c = 1000 - a - b;
            if (a*a + b*b == c*c) {
                result = a*b*c;
                return result;
            }
        }
    }
    
    return 0; // If no number has been found
}
