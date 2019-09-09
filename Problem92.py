'''

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

'''

def nextNumber(number):
	r = 0
	for n in str(number):
		r += int(n)**2
	return r


def updateLookUp(arr,value):
	for n in arr:
		lookUp[n] = value

def is89(number,arr,prev):
	# We do a shortcut: If only the last digit is changing, we can directly calculate whether the value ends at 89 (at least for large numbers)
	if number > 1000:
		l = number % 10
		if l != 0:
			curr = prev - (l-1)**2 + l**2
			if lookUp[curr] == 89:
				return True, curr
			else:
				return False, curr

	# Base case: We know the value already
	if number in lookUp:
		if lookUp[number] == 89:
			updateLookUp(arr,89)
			return True, arr[-1]
		else:
			updateLookUp(arr,1)
			return False, arr[-1]

	n = nextNumber(number)
	arr.append(n)
	return is89(n,arr,prev)


if __name__ == '__main__':
	count = 0
	lookUp = {1:1,44:1,32:1,13:1,10:1,85:89,145:89,42:89,20:89,4:89,16:89,37:89,58:89,89:89}
	isCandidate = False
	prev = 0

	for i in range(1,10**7):
		isCandidate, prev = is89(i,[i],prev)
		if isCandidate:
			count += 1
	print(count)
