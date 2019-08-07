'''

Project Euler Problem 52:

There are exactly ten ways of selecting three from five, 12345:

	123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3=10

In general, nCr = n!/(r!(n−r)!) , where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: 23C10=1144066.

How many, not necessarily distinct, values of nCr for 1≤n≤100 , are greater than one-million?

'''


def binomial(n,r):
	if r>n-r:
		return factorial(n,r)/factorial(n-r)
	else:
		return factorial(n,n-r)/factorial(r)

def factorial(n,limit=0):
	factorial = 1
	while n>limit:
		factorial *= n
		n-=1
	return factorial


def problem53():
	sumOneMillion = 0
	for n in range(23,101):
		for r in range(0,n+1):
			binom = binomial(n,r)
			if binom > 1e6:
				sumOneMillion += 1
	return sumOneMillion


print('Solution is: {}'.format(problem53()))

