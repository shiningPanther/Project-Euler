'''
Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

# Number to get prime factors of
# Note: In Python 3 the integer is unlimited in size, equivalent to a long integer in Python 2.7
# contd: In Python 2.7 the integer size depends on the word size of the CPU, which is in my case (I think) 64 bit. In order to work with larger numbers one needs to declare the long variable.
N = 600851475143

# Get the prime numbers
primeFactors = []
# We only need to iterate through all the numbers until the squared value is the same as the number to test
i = 1
while (i*i) <= N:
	i += 1
	if N % i == 0:
		# Check if the dividers are really a prime number
		# testList gives a 0 entry if the new number is not a prime number 
		testList = [i % x for x in primeFactors]
		if 0 not in testList:
			primeFactors.append(i)

print('Number:', N)
print('Prime factors:', primeFactors)
