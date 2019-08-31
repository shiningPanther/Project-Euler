'''

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

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
	maxNumber = int(N**0.5) + 1
	for number in range(5,maxNumber,2):
		if isPrime(number):
			primeArray.append(number)
	return primeArray


def getPrimeFactor(number,primeArray,primeFactors):
	if number in primeFactors:
		return primeFactors[number]
	for prime in primeArray:
		if number % prime == 0:
			if number/prime == 1:
				primeFactors[number] = [prime]
			else:
				otherPrimes = getPrimeFactor(number/prime,primeArray,primeFactors)
				if prime in otherPrimes:
					primeFactors[number] = otherPrimes
				else:
					primeFactors[number] = [prime] + otherPrimes
			break
		if prime > number ** 0.5:
			primeFactors[number] = [number]
			break

def isCandidate(i,primeFactors):
	for fac in primeFactors[i]:
		if fac in primeFactors[i-1]:
			return False
	return True


if __name__ == '__main__':
	primeArray = getPrimes(10**6)
	primeFactors = {}
	solutionFound = False
	i = 1
	length = 4
	while not solutionFound:
		i+=1
		getPrimeFactor(i,primeArray,primeFactors)
		if len(primeFactors[i]) == length and len(primeFactors[i-1]) == length and len(primeFactors[i-2]) == length and len(primeFactors[i-3]) == length:
			for j in range(length):
				if not isCandidate(i-j,primeFactors):
					break
				if j == length -1:
					solutionFound = True
					print(i-3)






