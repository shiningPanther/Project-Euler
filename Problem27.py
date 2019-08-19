'''

Euler discovered the remarkable quadratic formula:

n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
However, when n=40, 40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41, 41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form: n^2+an+b, where |a|<1000 and |b|≤1000,
where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0

'''


def getPrimes(N):
	primeArray = [2,3] # 2 and 3 are primes
	primeDict = {0:False, 1:False,2:True,3:True,4:False}
	maxNumber = N + 1
	for number in range(5,maxNumber,1):
		if isPrime(number,primeArray):
			primeArray.append(number)
			primeDict[number] = True
		else:
			primeDict[number] = False
	return primeArray, primeDict

def isPrime(n,primeArray):
	for prime in primeArray:
		if n % prime == 0:
			return False
		if prime*prime > n:
			return True
	return True


if __name__ == '__main__':
	N = 20000
	primeArray, primeDict = getPrimes(N)
	maxN = 1
	maxA = 0
	maxB = 0
	for b in primeArray:
		if b > 1000:
			break
		for a in range(-999,1000):
			if 1 + a + b <= 1:
				continue
			for n in range(100):
				number = n**2 + a*n + b	
				if number < 0:
					if n > maxN:
						maxA = a
						maxB = b
						maxN = n
					break
				if not primeDict[number]:
					if n > maxN:
						maxA = a
						maxB = b
						maxN = n
					break
	print(maxA*maxB)
	print(maxN)
	








