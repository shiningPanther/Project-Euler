'''
The proper divisors of a number are all the divisors excluding the number itself. 
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. 
As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, 
forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
'''

import numpy as np
from timeit import default_timer as timer

def sum_of_divisors(n):
	count = 1
	for i in range(2,int(np.sqrt(n))+1):
		if n % i == 0:
			count += i
			if i*i != n:
				count += n / i
	return int(count)


start = timer()
notAmicable = {1:0}
amicable = {}
longest_chain = []
N = 10**6
for n in range(N):
	if n in notAmicable:
		continue
	if n in amicable:
		continue
	s = n
	chain = [s]
	while True:
		s = sum_of_divisors(s)
		if s == n:
			print(n,'This number is amicable')
			for c in chain:
				amicable[c] = 1
			if len(chain) > len(longest_chain):
				longest_chain = chain
				print(chain)
			break
		if s in amicable or s in notAmicable or s > N:
			for c in chain:
				notAmicable[c] = 0
			break
		if s in chain:
			notAmicable[n] = 0
			break
		chain.append(s)

end = timer()
print('Time elapsed: {}s'.format(end-start))
