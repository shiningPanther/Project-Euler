'''

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

'''


import numpy as np


def lengthChain(number,lookUp):
	if number in lookUp:
		return lookUp[number]
	if number % 2 == 0:
		a = 1 + lengthChain(number/2,lookUp)
	else:
		a = 2 + lengthChain((3*number+1)/2, lookUp)
	lookUp[number] = a
	return a

if __name__ == '__main__':

	lookUp = {1:1}
	maxLength = 1
	maxNumber = 1
	for i in range(int(0.5*1e6),int(1e6)):
		length = lengthChain(i,lookUp)
		if length > maxLength:
			maxLength = length
			maxNumber = i
	print(maxNumber)
	print(maxLength)
