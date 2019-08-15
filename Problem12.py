import time


def getDivisors(number):
	divisors = [1, number] # One and its own number - does not work for 1 but doesn't matter
	if number % 2 != 0:
		return []
	if number % 3 != 0:
		return []
	if number % 4 != 0:
		return []
	if number % 5 != 0:
		return []

	for i in range(2, int(number**0.5)+1):
		if number % i == 0:
			divisors.append(i)
			divisors.append(number/i)

	return divisors

def findTriangleNumbers(N):
	triangleNumber = 1
	i = 1
	while True:
		i += 1
		triangleNumber = triangleNumber + i
		divisors = getDivisors(triangleNumber)
		if len(divisors) > N:
			return triangleNumber
			



if __name__ == '__main__':
	divisors = 500
	print(findTriangleNumbers(divisors))