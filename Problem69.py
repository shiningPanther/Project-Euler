'''

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

'''


if __name__ == '__main__':
	# It is obvious that the number that consists of the product of as many prime factors as possible minimizes this sum.
	# Furthermore, the prime factors need to be as small as possible to minimise n as well.

	print(2*3*5*7*11*13*17)



