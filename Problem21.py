'''

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''

def getSomeOfDivisors(n):
	sumDivisors = 1
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			sumDivisors += i
			sumDivisors += n / i
			if i**2 == n:
				sumDivisors -= i
	return sumDivisors




def getAmicable(N):
	done = {}
	amicableNumbers = []
	for i in range(2,N):
		done[i] = False
	for number in range(2,N):
		if not done[number]:
			sumDivisors1 = getSomeOfDivisors(number)
			done[number] = True
			if sumDivisors1 == 1:
				continue
			if sumDivisors1 >= N:
				continue
			if not done[sumDivisors1]:
				sumDivisors2 = getSomeOfDivisors(sumDivisors1)
				if number == sumDivisors2:
					amicableNumbers.append(sumDivisors1)
					amicableNumbers.append(sumDivisors2)
	return amicableNumbers


if __name__ == '__main__':
	print(sum(getAmicable(10000)))