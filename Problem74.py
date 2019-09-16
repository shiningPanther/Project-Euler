'''

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

'''

def n_repetitions(s,repetitions,factorials):
	if s in repetitions:
		return repetitions[s]
	x = 0
	for c in s:
		x += factorials[c]
	s_new = str(x)
	if s_new == s:
		return 1
	a = 1 + n_repetitions(s_new,repetitions,factorials)
	repetitions[s] = a
	return a

def factorial(x):
	if x == 0:
		return 1
	fac = 1
	while x > 0:
		fac *= x
		x-=1
	return fac

def main():
	factorials = {str(x):factorial(x) for x in range(0,10)}
	repetitions = {'169':3,'363601':3,'1454':3,'871':2,'45361':2,'872':2,'45362':2}
	count = 0
	for x in range(1,10**6):
		n = n_repetitions(str(x),repetitions,factorials)
		if n == 60:
			count+=1
	print(count)

if __name__ == '__main__':
	main()




