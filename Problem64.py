'''

All square roots are periodic when written as continued fractions and can be written in the form:

√N=a0+1a1+1a2+1a3+…

Exactly four continued fractions, for N≤13, have an odd period.

How many continued fractions for N≤10000 have an odd period?

'''

import numpy as np

def period(n):

	def continuedFraction(number,multiplier,rest):
		divisor = (number-rest**2)/multiplier
		rest -= divisor
		a = 1
		while rest > 0 or (rest-divisor)**2 < number:
			rest = rest - divisor
			a += 1
		rest = -rest
		contFractions.append((a,divisor,rest))
		return a,divisor,rest


	i = 0
	while (i+1)**2 <= n:
		i+=1
	if i**2 == n:
		return 0
	else:
		contFractions = []
		multiplier = 1
		a = 0
		rest = i
		period = 0
		while True:
			a,multiplier,rest = continuedFraction(n,multiplier,rest)
			if period != 0 and (a,multiplier,rest) == contFractions[0]:
				return period
			period += 1

def main():
	count = 0
	for i in range(1,10001):
		if period(i)%2 != 0:
			count+=1
	print(count)



if __name__ == '__main__':
	main()

