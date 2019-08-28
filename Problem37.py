'''

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''

def addPrime(primeArray):

	def isPrime(n):
		for prime in primeArray:
			if n % prime == 0:
				return False
			if prime*prime > n:
				return True

	i = 0
	while True:
		i += 1
		number = primeArray[-1] + i
		if isPrime(number):
			primeArray.append(number)
			break

def isTruncatable(prime,primeArray):
	s = str(prime)
	n = len(s)

	# Check for breaking conditions
	breakArray = [1,4,6,8,9]
	if prime % 10 in breakArray:
		return False
	if prime // (10**(n-1)) in breakArray:
		return False

	# Truncate from right side
	ss = s
	while True:
		if len(ss) == 1:
			break
		ss = ss[:-1]
		if int(ss) not in primeArray:
			return False

	# Truncate from left side
	ss = s
	while True:
		if len(ss) == 1:
			break
		ss = ss[1:]
		if int(ss) not in primeArray:
			return False
	return True


if __name__ == '__main__':
	primes = [2,3,5,7]
	count = 0
	truncatables = []
	while count < 11:
		addPrime(primes)
		if isTruncatable(primes[-1],primes):
			count += 1
			truncatables.append(primes[-1])
	print(truncatables)
	print(sum(truncatables))


