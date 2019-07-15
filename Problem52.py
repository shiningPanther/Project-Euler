'''

Project Euler Problem 52:

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''


print('Script started')


def containSameDigits(number1, number2):
	dictionary1 = {}
	for char in str(number1):
		if char in dictionary1:
			dictionary1[char] += 1
		else: 
			dictionary1[char] = 0

	dictionary2 = {}
	for char in str(number2):
		if char in dictionary2:
			dictionary2[char] += 1
		else: 
			dictionary2[char] = 0	

	if dictionary1 == dictionary2:
		return True

	return False



def problem52():
	exponentMax = 7
	for exponent in range(2,exponentMax):
		for i in range(10**(exponent-1),10**exponent):
			if 6*i > 10**exponent:
				break
			if not containSameDigits(i,2*i):
				continue
			if not containSameDigits(i,3*i):
				continue
			if not containSameDigits(i,4*i):
				continue
			if not containSameDigits(i,5*i):
				continue
			if containSameDigits(i,6*i):
				return i

	return ('No solution found')


print('Solution is: {}'.format(problem52()))

print('Script ended')
