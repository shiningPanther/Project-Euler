'''

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

'''

def getPrimes(N=1000):
	primeArray = [2,3] # 2 and 3 are primes
	maxNumber = int(N) + 1
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



def n_ways(n,primeIndex,primes,sums):
	if n==0:
		return 1
	if n==1:
		return 0
	if n==2:
		return 1
	
	prime = primes[primeIndex]
	while prime>n:
		primeIndex-=1
		prime = primes[primeIndex]
	if n in sums and prime in sums[n]:
		return sums[n][prime]

	a=0
	temp_prime = prime
	while primeIndex>=0:
		b = n_ways(n-temp_prime,primeIndex,primes,sums)
		primeIndex-=1
		temp_prime = primes[primeIndex]
		a+=b

	if n in sums:
		sums[n][prime] = a
	else:
		sums[n] = {}
		sums[n][prime] = a
	return a



def main():
	primes = getPrimes()
	sums = {}
	n = 10
	res = 0
	while res < 5000:
		for i in range(len(primes)):
			if primes[i] > n:
				primeIndex=i-1
				break
		res = n_ways(n,primeIndex,primes,sums)
		print(n,res)
		n+=1

if __name__ == '__main__':
	main()




