'''

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

'''

def getPrimes(N):
	primeArray = [2,3] # 2 and 3 are primes
	maxNumber = int(N**0.5) + 100
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

def getFourths(N,primes):
	fourth=[]
	for prime in primes:
		n=prime**4
		if n > N:
			break
		fourth.append(n)
	return fourth

def getThirds(fourthPowers,N,primes):
	third=[]
	for fourth in fourthPowers:
		for prime in primes:
			n = prime**3
			if n > N:
				break
			m = n+fourth
			if m > N:
				break
			third.append(m)
	return third

def getSeconds(thirdPowers,N,primes):
	secondDict={}
	second=[]
	for third in thirdPowers:
		for prime in primes:
			n = prime**2
			if n>N:
				break
			m = n+third
			if m>N:
				break
			if m in secondDict:
				continue
			second.append(m)
			secondDict[m]=1
	return second


def main():
	N = 50*10**6
	primes=getPrimes(N)
	fourthPowers = getFourths(N,primes)
	thirdPowers = getThirds(fourthPowers,N,primes)
	secondPowers = getSeconds(thirdPowers,N,primes)
	print(len(secondPowers))



if __name__ == '__main__':
	main()




