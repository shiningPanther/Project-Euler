'''

The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

'''

def counter(n):
	count = 0
	number = 0
	while len(str(number**n)) <= n:
		number+=1
		length = len(str(number**n))
		if length == n:
			count+=1
	return count


if __name__ == '__main__':
	n = 1
	count = 0
	while len(str(2**n)) <= n:
		count += counter(n)
		print(n,count)
		n+=1











