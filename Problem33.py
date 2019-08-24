'''

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe 
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''


def isCuriousFraction(numerator,denominator):
	digitNumerator = [numerator//10,numerator%10]
	digitDenominator = [denominator//10,denominator%10]
	containSameDigit = False
	for num in digitNumerator:
		if num == 0:
			continue
		elif num in digitDenominator:
			digitNumerator.remove(num)
			digitDenominator.remove(num)
			containSameDigit = True
			break
	if containSameDigit:
		if digitDenominator[0] == 0:
			return False
		if digitNumerator[0]/digitDenominator[0] == numerator/denominator:
			return True
	else:
		return False


if __name__ == '__main__':
	curiousFractions = []
	for numerator in range(10,100):
		for denominator in range(numerator+1, 100):
			if isCuriousFraction(numerator,denominator):
				curiousFractions.append((numerator,denominator))
	print(curiousFractions)

