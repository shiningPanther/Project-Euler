'''

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

'''

def getPrimes(N):
	primeArray = [2,3] # 2 and 3 are primes
	maxNumber = int(N**0.5) + 1
	for number in range(5,maxNumber,2):
		if isPrime(number,primeArray):
			primeArray.append(number)
	return primeArray

def isPrime(n,primeArray):
	if n == 1:
		return False
	for prime in primeArray:
		if n % prime == 0:
			return False
		if prime*prime > n:
			return True
	return True

def getPrimeFactors(number,primeArray,primeFactors):
	primeFactors[number] = []
	for prime in primeArray:
		if number % prime == 0:
			primeFactors[number].append(prime)
			if prime*prime != number and isPrime(number/prime,primeArray):
				primeFactors[number].append(number/prime)
				break
			for i in primeFactors[number/prime]:
				if i not in primeFactors[number]:
					primeFactors[number].append(i)
			break
	return primeFactors

def n_irreducible(number,primeFactors):
	if primeFactors[number] == []:
		return number-1
	count = number
	for prime in primeFactors[number]:
		count *= (1-1/prime)
	return int(count)


def main():
	N=10**6
	primeArray = getPrimes(N)
	primeFactors = {}
	count = 0
	for i in range(1,N+1):
		getPrimeFactors(i,primeArray,primeFactors)
		count += n_irreducible(i,primeFactors)
	print(count)

if __name__ == '__main__':
	main()




