'''

A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: 
N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. 
The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

'''

import numpy as np

def getPrimes(N):
	primeArray = [2,3] # 2 and 3 are primes
	maxNumber = int(N/2) + 1
	for number in range(5,maxNumber,2):
		if isPrime(number,primeArray):
			primeArray.append(number)
	return primeArray

def isPrime(n,primeArray):
	for prime in primeArray:
		if n % prime == 0:
			return False
		if prime*prime > n:
			return True
	return True

def primeFactors(number,primeArray):
	primeFactors = []
	for prime in primeArray:
		if prime >= number: # This can be improved a bit here...
			break
		if number % prime == 0:
			primeFactors.append(prime)
			a=1
			while True:
				if number % prime**(a+1) == 0:
					primeFactors.append(prime)
					a+=1
				else:
					break
	return primeFactors

def getK(factors):
	sumFactors = sum(factors)
	prodFactors = np.prod(factors)
	nFactors = len(factors)
	return prodFactors-sumFactors+nFactors

def addDict(k,number):
	if k-1 in kDict:
		kDict[k-1].append(number)
	else:
		kDict[k-1]=[number]

def canRepresent(kdiff,number):
	for i in range(kdiff,0,-1):
		if i not in kDict:
			continue
		for div in kDict[i]:
			if number % div == 0:
				if i == kdiff:
					return True
				else:
					if canRepresent(kdiff-i,number/div):
						return True
	return False

if __name__ == '__main__':
	N = 2*10**4
	primes=getPrimes(N)
	klist=list(range(2,12001))
	kDict={} # A dictionary that stores the max k value for all numbers - this is important since any number can be reduced by this k-1 if it is divisible by this number
	numberSet = set()
	number=3

	while klist != []:
		number+=1
		currentK = klist[0]
		factors = primeFactors(number,primes)
		if factors == []:
			continue
		k = getK(factors)
		addDict(k,number)
		if k == currentK:
			numberSet.add(number)
			klist.pop(0)
			print(currentK,number)
		elif k > currentK:
			if k in klist:
				numberSet.add(number)
				klist.remove(k)
				print(k,number)
			i=0
			while currentK < k:
				i+=1
				kdiff=k-currentK
				if canRepresent(kdiff,number):
					numberSet.add(number)
					klist.remove(currentK)
					i-=1
					print(currentK,number)
				if i>=len(klist):
					break
				currentK=klist[i]

	print(sum(numberSet))


