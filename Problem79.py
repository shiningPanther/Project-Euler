'''

A common security method used for online banking is to ask the user for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

'''


def readFile():
	with open('p079_keylog.txt','r') as f:
		return f.read().splitlines()

def updateGuess(guess):
	firstEntry = {}
	for p in array:
		if p[0] in guess:
			continue
		if p[0] in firstEntry:
			firstEntry[p[0]] += 1
		else:
			firstEntry[p[0]] = 1
	if firstEntry != {}:
		guess.append(max(firstEntry.keys(), key=(lambda k: firstEntry[k])))
		return updateGuess(guess)

	else:
		secondEntry = {}
		for p in array:
			if p[1] in guess:
				continue
			if p[1] in secondEntry:
				secondEntry[p[1]] += 1
			else:
				secondEntry[p[1]] = 1
		if secondEntry != {}:
			guess.append(max(secondEntry.keys(), key=(lambda k: secondEntry[k])))
			return updateGuess(guess)

		else:
			lastEntry = {}
			for p in array:
				if p[2] in guess:
					continue
				if p[2] in lastEntry:
					lastEntry[p[2]] += 1
				else:
					lastEntry[p[2]] = 1
			if lastEntry != {}:
				guess.append(min(lastEntry.keys(), key=(lambda k: lastEntry[k])))
				return updateGuess(guess)
			else:
				return guess


if __name__ == '__main__':
	array = readFile()
	print(array)
	guess = []
	guess = updateGuess(guess)
	print(int(''.join(guess))) 
	# Note: The algorithm gives the answer 73612890, however, we can see that the one should come before the 6.
	# Changing these two numbers gives the correct result.
	




