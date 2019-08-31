'''

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''


def getPrimeArray(N):

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

def isGoldbach(n):
	for prime in primes:
		if prime > n:
			break
		for i in range(int((n/2)**0.5)+1):
			s = prime + 2*i**2
			if s == n:
				return True
			if s > n:
				break
	return False


if __name__ == '__main__':
	N = 10**4
	primes = getPrimeArray(N)
	n = 33
	while True:
		if not isGoldbach(n):
			print(n)
			break
		n+=2








