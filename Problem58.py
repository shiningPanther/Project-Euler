'''

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers 
lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

'''


def getPrimes(N):
	primeArray = [2,3] # 2 and 3 are primes
	primeDict = {2:True,3:True}
	maxNumber = N + 1
	for number in range(4,maxNumber,2):
		primeDict[number]=False
	for number in range(5,maxNumber,2):
		if isPrime(number,primeArray):
			primeArray.append(number)
			primeDict[number] = True
		else:
			primeDict[number] = False
	return primeArray

def isPrime(n,primeArray):
	for prime in primeArray:
		if n % prime == 0:
			return False
		if prime*prime > n:
			return True
	return True


if __name__ == '__main__':
	N = 10**5
	primeArray = getPrimes(N)
	ratio = 100
	primes = 0
	nonPrimes = 1
	length = 3
	number = 1
	counter = 0
	while ratio >= 10:
		number+=length-1
		if isPrime(number,primeArray):
			primes+=1
		else:
			nonPrimes+=1
		if nonPrimes != 1:
			ratio = primes/(primes+nonPrimes)*100
		counter += 1
		if counter == 4:
			counter = 0
			length += 2
	
	if counter == 0:
		print(length-2)
	else:
		print(length)




