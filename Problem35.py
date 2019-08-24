'''

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''


def getCandidates(N):

	def isPrime(n):
		for prime in primeArray:
			if n % prime == 0:
				return False
			if prime*prime > n:
				return True
		return True
	
	primeArray = [2,3] # 2 and 3 are primes
	candidateArray = [2,3,5]
	maxNumber = int(N) + 1
	for number in range(5,maxNumber,2):
		if isPrime(number):
			primeArray.append(number)
			if isCandidate(number):
				candidateArray.append(number)

	return candidateArray

def isCandidate(prime):
	nonPrimes = [0,2,4,5,6,8]
	primeDigits = [int(x) for x in str(prime)]
	for nonPr in nonPrimes:
		if nonPr in primeDigits:
			return False
	return True

def isCircular(candidate):
	digits = [int(x) for x in str(candidate)]
	for i in range(len(digits)):
		if len(digits) == 1:
			return True
		else:
			s = [str(x) for x in digits[i:]] + [str(x) for x in digits[:i]]
			rotation = int(''.join(s))
			if rotation not in candidates:
				return False
	return True


if __name__ == '__main__':
	circularPrimes = []
	N = 10**6
	candidates = getCandidates(N)
	for candidate in candidates:
		if candidate not in circularPrimes and isCircular(candidate):
			circularPrimes.append(candidate)
	print(circularPrimes)
	print(len(circularPrimes))



