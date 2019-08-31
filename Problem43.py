'''

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

'''

def updateComb(number,divisor,output):
	digits = [0,1,2,3,4,5,6,7,8,9]
	if len(number) == 2:
		number = '0' + number
	for digit in str(number):
		try:
			digits.remove(int(digit))
		except:
			return False
	for j in digits:
		temp = str(j)+number[:2]
		if int(temp) % divisor == 0:
			output.append(str(j)+number)


if __name__ == '__main__':
	comb8910 = []
	comb789 = []
	comb678 = []
	comb567 = []
	comb456 = []
	comb345 = []
	comb234 = []
	combTot = []
	for i in range(17,1000,17):
		comb8910.append(str(i))
	for i in range(len(comb8910)):
		updateComb(comb8910[i],13,comb789) 
	for i in range(len(comb789)):
		updateComb(comb789[i],11,comb678)
	for i in range(len(comb678)):
		updateComb(comb678[i],7,comb567)
	for i in range(len(comb567)):
		updateComb(comb567[i],5,comb456)
	for i in range(len(comb456)):
		updateComb(comb456[i],3,comb345)
	for i in range(len(comb345)):
		updateComb(comb345[i],2,comb234)
	for i in range(len(comb234)):
		updateComb(comb234[i],1,combTot)
	print(comb789)
	print(comb678)
	print(comb567)
	print(comb456)
	print(comb345)
	print(comb234)
	print(combTot)
	print(sum(int(x) for x in combTot))
	





