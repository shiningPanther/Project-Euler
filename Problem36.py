'''

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

'''

import numpy as np

def getPalindromes():
	pal = [1,2,3,4,5,6,7,8,9]
	digits = 2
	while digits < 7:
		for i in range(10**(digits//2-1),10**(digits//2)):
			if digits%2 == 0:
				s = str(i) + str(i)[::-1]
				pal.append(int(s))
			else:
				for j in range(1,10):
					s = str(i) + str(j) + str(i)[::-1]
					pal.append(int(s))
		digits+=1
	return pal

def isPalBase2(pal):

	def getBase2(number):
		s = []
		n = int(np.log(number)/np.log(2))
		while n>=0:
			if 2**n <= number:
				s.append('1')
				number-=2**n
			else:
				s.append('0')
			n-=1
		return s

	def isPal(number):
		if len(number) % 2 == 0:
			if number[:len(number)//2] == number[:len(number)//2-1:-1]:
				return True
		else:
			if number[:len(number)//2] == number[:len(number)//2:-1]:
				return True
		return False

	base2 = getBase2(pal)
	if isPal(base2):
		return True
	else:
		return False

if __name__ == '__main__':
	sumPal = 0
	palindromes = getPalindromes()
	for pal in palindromes:
		if isPalBase2(pal):
			sumPal += pal
	print(sumPal)




