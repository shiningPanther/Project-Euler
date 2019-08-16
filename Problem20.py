'''

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''

def factorial(n):
	digitArray = [1]
	while n > 1:
		carry = 0
		for i in range(len(digitArray)-1,-1,-1):
			a = digitArray[i] * n + carry
			digitArray[i] = a % 10
			carry = a // 10

			if carry >= 10 and i == 0:
				digitArray.insert(0, carry%10)
				digitArray.insert(0, carry//10)
			elif carry > 0 and i == 0:
				digitArray.insert(0, carry)
		n-=1
	return digitArray


if __name__ == '__main__':
	print(sum(factorial(100)))