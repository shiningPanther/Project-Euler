'''
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

divisibleUntil = 20
# Put an upper limit so that the loop does not go forever in case something does not work as intended
upperLimit = 1000000000


def isEvenlyDivisible(number, divisibleUntil):
	for divisor in range(divisibleUntil,1,-1):
		# We start from the largest divisor - if that returns false we stop immediately
		if not number % divisor == 0:
			return False
	return True

# We only iterate through numbers that are a multiple of the largest divisor
for number in range(divisibleUntil, upperLimit, divisibleUntil):
	# We don't need to check for the largest divisor since the number is already a multiple of that one
	if isEvenlyDivisible(number, divisibleUntil-1):
		print(number)
		break



