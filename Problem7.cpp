/*
 By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 
 What is the 10 001st prime number?
*/


#include "Problem7.h"
#include <iostream>

int Problem7() {
    const int N = 10001; // N is the Nth prime number to be searched
    int primes [N] {2}; // initalize the array of primes (with 2 being the first prime)
    int stop = 1e7; // only iterate through numbers until here
    int primeCount = 1;
    
    // We iterate through all the natural numbers. The stop saves us in case sth goes wrong.
    for (int number = 3; number<stop; number++) {
        // In this for loop we divide the numbers by all the primes to determine if it is another prime.
        // Once the modulus is 0 we it is not a prime and we step out of the function. If not, it is a prime.
        for (int i = 0; i<primeCount; i++) {
            if (number % *(primes+i) == 0) {
                break;
            }
            else if (i == primeCount - 1) {
                primes [primeCount] = number;
                primeCount++;
            }
        }
        if (primeCount == N) {break;} // break once we found the wanted prime number.
    }
    
    return primes[N-1];
    
}
