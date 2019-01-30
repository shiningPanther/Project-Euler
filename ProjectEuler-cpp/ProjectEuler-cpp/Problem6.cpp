/*
 Problem 6:
 
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
 
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
 
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

#include "Problem6.h"
#include <iostream>

int Problem6() {
    int N = 100;
    int sumOfSquares = 0;
    int sum = 0;
    for (int i=1; i<=N; i++) {
        sumOfSquares += i*i;
        sum += i;
    }
    return sum*sum - sumOfSquares;
}
