/*
 By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
 
 By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
 
 Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
 */


#include "Problem51.h"
#include <iostream>
#include <math.h>
using namespace std;


/* SEVERAL THOUGHTS
 1. Later on, we need to check if a number is a prime and already have an array that lists all the primes. It is MUCH faster to calculate again if this number is a prime than looking through the entire array
 2. We are looking for an 8 prime value family. This can only be achieved by replacing 3 (or maybe more) digits. With two digits this is not possible, since every third time that the two digits are changed, the number can be divided by three, making the maximum family to achieve a 7 prime value family
 */



int numberOfPrimes = 1000000;

int Problem51() {

    int primeArray[numberOfPrimes];
    
    getPrimes(primeArray);
    
    /*for (int i = 0; i<numberOfPrimes; i++) {
        cout << primeArray[i] << "\n";
    }*/
    
    int smallestPrimeNumber = getSmallestPrime(primeArray, 8);
    
    return smallestPrimeNumber;
}

// We look at each number in the prime array that has 7 digits and replace one digit by another number
int getSmallestPrime(int *primeArray, int numberPrimeFamily) {
    
    // Go through the primeArray
    for (int i=0; i<numberOfPrimes; i+=1) {
        
        // First check that we only look at the 5 - 7 digit numbers
        if (*(primeArray+i) < 10000 || *(primeArray+i) > 10000000) {continue;}
        
        // Now, check the number of digits of the prime number
        int digits = 0;
        int number = *(primeArray+i);
        while (number) {
            number /=10;
            digits ++;
        }
        
        // First, convert the number into a charArray (string)
        char numberString[digits];
        intToString(*(primeArray+i), digits, numberString);
        
        // Now look for numbers that are repeating (here, only three equal numbers are considered)
        for (int j=0; j<digits-3; j++) {
            for (int k=j+1; k<digits-2; k++) {
                for (int l=k+1; l<digits-1; l++) {
                    if (numberString[j] == numberString[k] && numberString[j] == numberString[l]) {
                        char possibleFamilyMemberString[digits];
                        strncpy(possibleFamilyMemberString, numberString, digits);
                        int numberOfTimesNotAPrime = 0;
                        // Now replace the number with another number
                        for (int newDigitCounter=0; newDigitCounter < 10; newDigitCounter ++) {
                            possibleFamilyMemberString[j] = newDigitCounter + '0';
                            possibleFamilyMemberString[k] = newDigitCounter + '0';
                            possibleFamilyMemberString[l] = newDigitCounter + '0';
                            int possibleFamilyMember = stringToInt(possibleFamilyMemberString, digits);
                            if (digits == 5 && possibleFamilyMember < 10000) {numberOfTimesNotAPrime+=1;continue;}
                            if (digits == 6 && possibleFamilyMember < 100000) {numberOfTimesNotAPrime+=1;continue;}
                            if (digits == 7 && possibleFamilyMember < 1000000) {numberOfTimesNotAPrime+=1;continue;}
                            if (!isPrime(primeArray, possibleFamilyMember)) {
                                numberOfTimesNotAPrime += 1;
                            }
                            if (numberOfTimesNotAPrime == 10 - numberPrimeFamily + 1) {break;}
                            if (newDigitCounter == 9) {
                                return *(primeArray+i);
                            }
                        }
                    }
                }
            }
        }
        
    }
    return 0;
}


void intToString(int number, int numberOfDigits, char* numberString) {
    if (numberOfDigits == 5) {
        numberString[0] = number / 10000 + '0';
        numberString[1] = number % 10000 / 1000 + '0';
        numberString[2] = number % 1000 / 100 + '0';
        numberString[3] = number % 100 / 10 + '0';
        numberString[4] = number % 10 + '0';
    }
    if (numberOfDigits == 6) {
        numberString[0] = number / 100000 + '0';
        numberString[1] = number % 100000 / 10000 + '0';
        numberString[2] = number % 10000 / 1000 + '0';
        numberString[3] = number % 1000 / 100 + '0';
        numberString[4] = number % 100 / 10 + '0';
        numberString[5] = number % 10 + '0';
    }
    if (numberOfDigits == 7) {
        numberString[0] = number / 1000000 + '0';
        numberString[1] = number % 1000000 / 100000 + '0';
        numberString[2] = number % 100000 / 10000 + '0';
        numberString[3] = number % 10000 / 1000 + '0';
        numberString[4] = number % 1000 / 100 + '0';
        numberString[5] = number % 100 / 10 + '0';
        numberString[6] = number % 10 + '0';
    }
}
    
int stringToInt(char* numberString, int numberOfDigits) {
    if (numberOfDigits == 5) {
        int number = (numberString[0] - '0') * 10000;
        number += (numberString[1] - '0') * 1000;
        number += (numberString[2] - '0') * 100;
        number += (numberString[3] - '0') * 10;
        number += (numberString[4] - '0');
        return number;
    }
    if (numberOfDigits == 6) {
        int number = (numberString[0] - '0') * 100000;
        number += (numberString[1] - '0') * 10000;
        number += (numberString[2] - '0') * 1000;
        number += (numberString[3] - '0') * 100;
        number += (numberString[4] - '0') * 10;
        number += (numberString[5] - '0');
        return number;
    }
    if (numberOfDigits == 7) {
        int number = (numberString[0] - '0') * 1000000;
        number += (numberString[1] - '0') * 100000;
        number += (numberString[2] - '0') * 10000;
        number += (numberString[3] - '0') * 1000;
        number += (numberString[4] - '0') * 100;
        number += (numberString[5] - '0') * 10;
        number += (numberString[6] - '0');
        return number;
    }
    return 0;
}

void getPrimes(int *primeArray) {
    
    int stop = 1e8; // only iterate through numbers until here
    *primeArray = 2; // The first prime is 2
    int primeCount = 1;
    
    // We iterate through all the natural numbers. The stop saves us in case sth goes wrong.
    for (int number = 3; number<stop; number += 2) {
        // In this for loop we divide the numbers by all the primes to determine if it is another prime.
        // Once the modulus is 0 we know it is not a prime and we step out of the function. If not, it is a prime.
        for (int i = 0; i<primeCount; i++) {
            // Once the number can get divided by any prime we get out of the loop
            if (number % *(primeArray+i) == 0) {break;}
            // Once the prime^2 is larger than the number we have a prime number
            if (*(primeArray+i) * *(primeArray+i) > number) {
                *(primeArray+primeCount) = number;
                primeCount++;
                break;
            }
        }
        if (primeCount == numberOfPrimes) {break;} // break once we found the wanted number of primes.
    }
}

bool isPrime(int *primeArray, int number) {
    for (int i=0; i<numberOfPrimes; i++) {
        if (number % *(primeArray+i) == 0) {return false;}
        if (*(primeArray+i)* *(primeArray+i) > number) {return true;}
    }
    return true;
}
