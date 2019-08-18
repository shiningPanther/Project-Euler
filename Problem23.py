'''

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number 
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''

'''

For mathematical explication of the solution, see:

https://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors

'''

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

def getSumDivisors(number,primeArray):
	sumDivisors = 1
	for prime in primeArray:
		if prime > number:
			break
		if number % prime == 0:
			a = 1
			while True:
				if number % prime**(a+1) == 0:
					a += 1
				else:
					break
			sumDivisors *= (prime**(a+1) - 1) / (prime - 1)
	return sumDivisors - number

def notSum(N,abundantNumbers):
	array = []
	for number in range(1,N):
		for i in abundantNumbers:
			if not abundantNumbers[i]:
				continue
			if 2*i > number:
				array.append(number)
				break
			a = number-i
			if abundantNumbers[a]:
				break
	return(array)


if __name__ == '__main__':
	N = 28123
	primeArray = getPrimes(N)
	abundantNumbers = {}
	for i in range(1,N+1):
		abundantNumbers[i] = getSumDivisors(i,primeArray) > i
	print(sum(notSum(N,abundantNumbers)))




