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
