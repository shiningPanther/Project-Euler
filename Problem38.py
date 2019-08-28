'''

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

'''

def isPandigital(number):
	i = 1
	pand = []
	while len(pand) < 9:
		digits = [x for x in str(number*i)]
		i+=1
		for digit in digits:
			if digit == '0':
				return 0
			if digit in pand:
				return 0
			pand.append(digit)
	return int(''.join(pand))




if __name__ == '__main__':
	maxPand = 0
	# All possible pandigital numbers are <10000
	for i in range(10**5):
		pand = isPandigital(i)
		if pand > maxPand:
			print(i,pand)
			maxPand = pand
	print(maxPand)



