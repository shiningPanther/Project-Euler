'''

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

'''

def getPrimes(N):

	def isPrime(n,primeArray):
		for prime in primeArray:
			if n % prime == 0:
				return False
			if prime*prime > n:
				return True
		return True

	primeArray = [2,3] # 2 and 3 are primes
	maxNumber = N
	for number in range(5,maxNumber,2):
		if isPrime(number,primeArray):
			primeArray.append(number)
	return primeArray

def isPermutation(n1,n2,n3):
	d1 = makeDict(n1)
	d2 = makeDict(n2)
	d3 = makeDict(n3)
	if d1 == d2 and d1 == d3:
		return True

def makeDict(n):
	p = {}
	for d in str(n):
		if d not in p:
			p[d] = 1
		else:
			p[d]+=1
	return p

if __name__ == '__main__':
	primeArray = getPrimes(10**4)
	for prime in primeArray:
		if prime < 10**3:
			continue
		for i in range(1000,5000):
			if prime + 2*i > 10**4:
				break
			if prime + i in primeArray and prime + 2*i in primeArray:
				if isPermutation(prime,prime+i,prime+2*i):
					print(prime,prime+i,prime+2*i)






