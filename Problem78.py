'''

Let p(n) represent the number of different ways in which n coins can be separated into piles. 
For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

'''

'''

To understand the way the solution is implemented, look up the Wikipedia article:
https://en.wikipedia.org/wiki/Partition_(number_theory)#Restricted_part_size_or_number_of_parts

'''


def p(n,p_dict):
	if n==0:
		return 1

	dif = lambda k: k*(3*k-1)/2
	k=1
	a=0
	while True:
		d=dif(k)
		if d>n:
			break
		if k%2 == 0:
			a-=p_dict[n-d]
		else:
			a+=p_dict[n-d]

		d=dif(-k)
		if d>n:
			break
		if k%2 == 0:
			a-=p_dict[n-d]
		else:
			a+=p_dict[n-d]
		k+=1

	a%=10**6
	p_dict[n] = a
	return a




def main():
	p_dict={0:1}
	sol = 1
	n=0
	while sol!=0:
		n+=1
		sol = p(n,p_dict)
	print(n)


	


if __name__ == '__main__':
	main()




