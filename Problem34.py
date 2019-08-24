'''

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''


def fillFactorials():
	for i in range(10):
		j = i
		fac = 1
		while i > 1:
			fac *= i
			i -= 1
		factorials[j] = fac

def isCurious(number):
	sumFac = 0
	for digit in str(number):
		sumFac+=factorials[int(digit)]
	if sumFac == number:
		return True
	else:
		return False



if __name__ == '__main__':
	numbers = []
	factorials = {}
	fillFactorials()
	for i in range(3,1000000):
		if isCurious(i):
			numbers.append(i)
	print(numbers)
	print(sum(numbers))

