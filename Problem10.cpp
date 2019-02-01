/*
 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 
 Find the sum of all the primes below two million.
*/


#include "Problem10.h"
#include <iostream>

long long Problem10() {
    int N = 2e6; // Primes until here
    int primes[200000] = {2}; // Arrays are static - to use dynamic variables a vector could be used. But I have enought memory and don't need to move around the values unnecessary. I fill this array with the first prime number (2) to start the calculations.
    int primeCount = 1; // Counts the number of primes. Needed to accesss the values in the array.
    long long primeSum = 2;
    
    // Loop through all the numbers and check if they can be divided by the primes until sqrt(number). If not they are a prime number.
    for (int number = 3; number < N; number++) {
        for (int i = 0; i < primeCount; i++) {
            if (number % primes[i] == 0) {
                // is not a prime - go to the next number
                break;
            }
            if (primes[i]*primes[i] > number) {
                // is a prime
                primes[primeCount] = number;
                primeCount += 1;
                primeSum += number;
                break;
            }
        }
    }
    return primeSum;
}
