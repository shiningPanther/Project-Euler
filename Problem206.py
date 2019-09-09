'''

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,

where each “_” is a single digit.

'''

def match(number):
	s = str(number)
	return all(int(s[2*i]) == i+1 for i in range(9))


def main():
	# The last two digits of the searched number have to be 00. We can exclude them and only look for the smaller number
	Nmin = int((1.0203040506070809 * 10**16)**0.5)
	Nmax = int((1.9293949596979899 * 10**16)**0.5)
	# We only need to consider numbers that either end on 3 or 7
	n = Nmax - Nmax%10 + 7

	while not match(n**2):
		n -= 10
	print(n*10)
	

if __name__ == '__main__':
	main()
