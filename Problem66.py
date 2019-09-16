'''

Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

'''

import fractions as fr
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
		contFractions = [i]
		multiplier = 1
		a = 0
		rest = i
		period = 0
		while True:
			a,multiplier,rest = continuedFraction(n,multiplier,rest)
			if period != 0 and (a,multiplier,rest) == contFractions[1]:
				return contFractions[:-1]
			period += 1


def solutions(frac):

	def continuedFraction(i,frac):
		length = len(frac)
		if i >= length:
				j = i%length
		else:
			j = i
		f = fr.Fraction(1,frac[j][0])
		i-=1
		while i >=0:
			if i >= length:
				j = i%length
			else:
				j = i
			f = fr.Fraction(1,frac[j][0]+f)
			i-=1
		return f

	base = frac[0]
	frac = frac[1:]
	i = 0
	while True:
		yield base+continuedFraction(i,frac)
		i+=1


def main():
	maxNumerator = 1
	maxD = 1
	for D in range(2,1001):
		frac = period(D)
		if frac == 0:
			continue
		for fraction in solutions(frac):
			if fraction.numerator**2 - D*fraction.denominator**2 == 1:
				print(D, fraction.numerator,fraction.denominator)
				if fraction.numerator > maxNumerator:
					maxNumerator = fraction.numerator
					maxD = D
				break
	print(maxD)


if __name__ == '__main__':
	main()

