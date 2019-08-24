'''

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

'''

def isSum(numberArray):
	numberDict = {}

	def calculateSum():
		numberSum = 0
		for digit in numberArray:
			if digit not in numberDict:
				numberDict[digit] = 1
			else:
				numberDict[digit] += 1
			numberSum += digit**5
		return numberSum

	def updateDict(a):
		if a in numberDict:
			if numberDict[a] == 1:
				del(numberDict[a])
			else: numberDict[a] -= 1
			return True
		else:
			return False


	numberSum = calculateSum()
	if numberSum >= 10**6 or numberSum < 10**3:
		return 0
	else:
		if updateDict(numberSum//100000) and updateDict((numberSum%100000)//10000) and updateDict((numberSum%10000)//1000) and updateDict((numberSum%1000)//100) and updateDict((numberSum%100)//10) and updateDict(numberSum%10):
			return numberSum
		else:
			return 0


if __name__ == '__main__':
	sumNumber = []
	numberDict = {}
	for a in range(0,10):
		for b in range(a,10):
			for c in range(b,10):
				for d in range(c,10):
					for e in range(d,10):
						for f in range(e,10):
							numberArray = [a,b,c,d,e,f]
							number = isSum(numberArray)
							if number != 0:
								sumNumber.append(number)
	print(sumNumber)
	print(sum(sumNumber))

