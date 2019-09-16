'''

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''

def getPrimeArray(N):
	primeArray = [2,3] # 2 and 3 are primes
	maxNumber = int(N**0.5) + 1
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

def conc_isPrime(primeArray,prime1,prime2,prime3=None,prime4=None,prime5=None):

	def singleConc_isPrime(prime1,prime2):
		if prime1 == None or prime2 == None:
			return True
		if isPrime(int(str(prime1)+str(prime2)),primeArray) and isPrime(int(str(prime2)+str(prime1)),primeArray):
			return True
		return False

	if prime3==None:
		return singleConc_isPrime(prime1,prime2)
	if prime4==None:
		return singleConc_isPrime(prime1,prime3) and singleConc_isPrime(prime2,prime3)
	if prime5==None:
		return singleConc_isPrime(prime1,prime4) and singleConc_isPrime(prime2,prime4) and singleConc_isPrime(prime3,prime4)
	else:
		return singleConc_isPrime(prime1,prime5) and singleConc_isPrime(prime2,prime5) and singleConc_isPrime(prime3,prime5) and singleConc_isPrime(prime4,prime5)


def main():
	N = 10**8
	primeArray = getPrimeArray(N)
	length = len(primeArray)
	answerFound = False
	i = 0

	while not answerFound:
		i+=1
		prime1 = primeArray[i]

		for j in range(i+1,length):
			prime2 = primeArray[j]
			if conc_isPrime(primeArray,prime1,prime2):

				for k in range(j+1,length):
					prime3 = primeArray[k]
					if conc_isPrime(primeArray,prime1,prime2,prime3):

						for l in range(k+1,length):
							prime4=primeArray[l]
							if conc_isPrime(primeArray,prime1,prime2,prime3,prime4):

								for m in range(l+1,length):
									prime5=primeArray[m]
									if conc_isPrime(primeArray,prime1,prime2,prime3,prime4,prime5):
										answerFound = True
										print(prime1,prime2,prime3,prime4,prime5)
										print(prime1+prime2+prime3+prime4+prime5)


if __name__ == '__main__':
	main()

