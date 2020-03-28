'''

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

'''


def n_ways(n,term_max,sums):
	if n==0:
		return 1
	if n==1:
		return 1
	if term_max==1:
		return term_max
	if n in sums:
		if term_max > n and n in sums[n]:
			return sums[n][n]
		elif term_max in sums[n]:
			return sums[n][term_max]

	a = 0
	if term_max>n:
		term_max = n
	temp = term_max
	while temp>=1:
		b = n_ways(n-temp,temp,sums)
		temp-=1
		a+=b
	if n in sums:
		sums[n][term_max] = a
	else:
		sums[n] = {}
		sums[n][term_max] = a
	return a



def main():
	sums={}
	print(n_ways(100,99,sums))
	print(sums)

if __name__ == '__main__':
	main()




