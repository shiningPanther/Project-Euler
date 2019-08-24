'''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

'''

def getPrimes(N):

	def isPrime(n):
		for prime in primeArray:
			if n % prime == 0:
				return False
			if prime*prime > n:
				return True
		return True
	
	primeArray = [2,3] # 2 and 3 are primes
	maxNumber = int(N) + 1
	for number in range(5,maxNumber,2):
		if isPrime(number):
			primeArray.append(number)
	return primeArray





if __name__ == '__main__':
	N = 10**6
	primeArray = getPrimes(N)
	print(primeArray)