'''

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

'''

import fractions as fr

def main():

	min_diff=1
	for d in range(10**6-100,10**6+1):
		for n in range(int(0.4285*d),int(0.4286*d)):
			diff = fr.Fraction(3,7) - fr.Fraction(n,d)
			if diff > 0 and diff < min_diff:
				min_diff = diff
				print(fr.Fraction(n,d),min_diff)


if __name__ == '__main__':
	main()

