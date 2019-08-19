'''

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10 = 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

'''

# We need the decimal class to deal with such long decimal numbers...
from decimal import *

if __name__ == '__main__':
	# We set the precission to 1500 decimal points
	N = 1500
	getcontext().prec = N

	longestCycle = 5
	longestD = 0

	for d in range(1,1000):
		x = str(Decimal(1)/Decimal(d))
		sequenceFound = False
		i = 0

		while not sequenceFound:
			i+=1
			if i >= len(x)-5:
				break
			if x[i] == 0:
				continue
			else:
				sequence = x[i:i+5]

				for j in range(i+1,len(x)-5):
					if x[j:j+5] == sequence:
						sequenceFound = True
						cycle = j-i
						if cycle > longestCycle:
							longestCycle = cycle
							longestD = d
						break
	
	print('Value of d is {} with {}-long recurring cycle'.format(longestD,longestCycle))








