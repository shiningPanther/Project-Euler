'''

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

'''

def getPrimes(N):

	primeArray = [2,3] # 2 and 3 are primes
	primeDict = {2:True,3:True} 
	maxNumber = N
	for number in range(4,maxNumber,2):
		primeDict[number] = False
	for number in range(5,maxNumber,2):
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
	N = 10**6
	primeArray,primeDict = getPrimes(N)
	primesAsSum = {}
	maxTerms = 0
	for i,prime in enumerate(primeArray):
		if prime in primesAsSum:
			continue
		primeSum = 0
		count = 0
		while i < len(primeArray):
			primeSum+=primeArray[i]
			if primeSum > N:
				break
			i+=1
			count +=1
			if primeDict[primeSum] == True:
				primesAsSum[primeSum] = True
				if count > maxTerms:
					maxTerms = count
					print(primeSum,maxTerms)










