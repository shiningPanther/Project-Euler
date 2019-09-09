'''

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; 
see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

'''

def readRomans():
	with open('p089_roman.txt','r') as f:
		return f.read().splitlines()

def check(r,numeral,smaller,larger10,larger5):
	count = 0
	last = 0
	length = len(r)
	for i,s in enumerate(r):
		if s == numeral:
			# Ignore if the numeral is written as a subtraction from a larger numeral
			if i+1 != length and (r[i+1] == larger10 or r[i+1] == larger5):
				continue
			# Ignore if previously a smaller numeral was subtracted
			if i-1 >= 0 and r[i-1] == smaller:
				continue
			else:
				count +=1
				last = i 

	# We can only save numerals if the count is larger than 3			
	if count > 3:
		# Check if there was a V, L or D going ahead (respectively)
		if last-count >= 0 and r[last-count] == larger5:
			if count == 4:
				return 3
			else:
				return 0
		# Otherwise we can replace 4 numerals by using the subtraction rule
		else:
			if count == 4:
				return 2
	else:
		return 0


def main():
	roman = readRomans()
	saving_tot = 0
	for r in roman:
		saving_C = check(r,'C','X','M','D') 
		saving_X = check(r,'X','I','C','L')
		saving_I = check(r,'I','0','X','V')
		#print(r,saving_C,saving_X,saving_I)
		saving_tot = saving_tot + saving_C + saving_X + saving_I
	print(saving_tot)

if __name__ == '__main__':
	main()

