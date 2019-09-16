'''

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

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

def getPrimeFactors(number,primeArray):
	primeFactors = []
	n = number
	for prime in primeArray:
		if prime**2 > n:
			if n!=1 and n < number:
				primeFactors.append(n)
			break
		if n % prime == 0:
			primeFactors.append(prime)
			n /= prime
			while n % prime == 0:
				n /= prime
	return primeFactors

def fractionsInRange(number,primeFactors):
	n_min = number//3 + 1
	n_max = number//2
	count = 0
	if primeFactors == []:
		return n_max-n_min+1
	for k in range(n_min,n_max+1):
		for fac in primeFactors:
			if k % fac == 0:
				break
			if fac == primeFactors[-1]:
				count += 1
	return count


def main():
	N=12000
	primeArray = getPrimes(N)
	primeFactors = {}
	count = 0
	for n in range(4,N+1):
		primeFactors = getPrimeFactors(n,primeArray)
		count += fractionsInRange(n,primeFactors)
	print(count)

if __name__ == '__main__':
	main()




