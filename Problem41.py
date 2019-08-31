'''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''

def getPrimeArray(N):
	
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

def constructCandidates(base,permutations):
	candidates = []
	for i in range(permutations,0,-1):
		for j in range(permutations,0,-1):
			if j == i:
				continue
			for k in range(permutations,0,-1):
				if k == j or k == i:
					continue
				for l in range(permutations,0,-1):
					if l == k or l == j or l == i:
						continue
					candidates.append(int(str(base)+str(i)+str(j)+str(k)+str(l)))
	return candidates


if __name__ == '__main__':
	N = 10**5
	primeArray = getPrimeArray(N)
	candidates = constructCandidates(765,4) # We don't need to look at 9- and 8-digits pandigitals since they are always divisible by 3
	for n in candidates:
		if isPrime(n,primeArray):
			print(n)





