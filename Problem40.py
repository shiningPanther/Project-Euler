'''

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''

def findDigit(position,digit,totalLength):
	prevLength = totalLength - int(len(str(digit)))
	strDigit = str(digit)
	return int(strDigit[position-prevLength-1])


if __name__ == '__main__':
	n = 1
	digit = 1
	product = 1

	while n < 10:
		digit += 1
		n += len(str(digit))
	product*=findDigit(10,digit,n)
	while n < 10**2:
		digit += 1
		n += len(str(digit))
	product*=findDigit(10**2,digit,n)
	while n < 10**3:
		digit += 1
		n += len(str(digit))
	product*=findDigit(10**3,digit,n)
	while n < 10**4:
		digit += 1
		n += len(str(digit))
	product*=findDigit(10**4,digit,n)
	while n < 10**5:
		digit += 1
		n += len(str(digit))
	product*=findDigit(10**5,digit,n)
	while n < 10**6:
		digit += 1
		n += len(str(digit))
	product*=findDigit(10**6,digit,n)
	print(product)





