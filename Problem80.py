'''

It is well known that if the square root of a natural number is not an integer, then it is irrational. 
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

'''

import decimal as dec

def main():
	dec.getcontext().prec = 102
	root = dec.Decimal(0.5)
	total = 0
	for n in range(2,101):
		count=0
		if n in [4,9,16,25,36,49,64,81,100]:
			continue
		s=str(dec.Decimal(n)**root)[:-2]
		for c in s:
			if c == '.':
				continue
			count+=int(c)
		total+=count
	print(total)


if __name__ == '__main__':
	main()




