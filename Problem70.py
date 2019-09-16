'''

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

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
	reduced = number
	for prime in primeArray:
		if prime**2 > reduced:
			break
		if reduced % prime == 0:
			yield prime
			reduced /= prime
			while reduced % prime == 0:
				reduced /= prime
		if reduced < number and isPrime(reduced,primeArray):
			yield reduced
			break

	'''
	if number % prime == 0:
		primeFactors[number].append(prime)
		if prime*prime != number and isPrime(number/prime,primeArray):
			primeFactors[number].append(number/prime)
			break
		for i in primeFactors[number/prime]:
			if i not in primeFactors[number]:
				primeFactors[number].append(i)
		break
	'''

def getPhi(n,primeFactors):
	res = n-1
	length = len(primeFactors)
	for i in range(length):
		res = res-n/primeFactors[i]+1
		j = i+1
		while j < length:
			res = res+n/(primeFactors[i]*primeFactors[j])-1
			j+=1
	return res

def isPermutation(n1,n2):
	def giveDict(n):
		d = {}
		for s in str(int(n)):
			if s in d:
				d[s] += 1
			else:
				d[s] =1
		return d

	return giveDict(n1) == giveDict(n2) 


def main():
	N=10**8
	primeArray = getPrimes(N)
	maxRatio = 2
	length = len(primeArray)
	for i in range(length):
		prime1 = primeArray[i]
		for j in range(i,length):
			prime2 = primeArray[j]
			number = prime1*prime2
			if number > 10**7:
				break
			else:
				phi = getPhi(number,[prime1,prime2])
			if isPermutation(number,phi) and number/phi < maxRatio:
				maxRatio = number/phi
				print(number,phi,number/phi,prime1,prime2)

if __name__ == '__main__':
	main()




