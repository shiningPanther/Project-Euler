'''
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36**2. 
What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96**2. 
We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, 
neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, 
find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
'''

from timeit import default_timer as timer
import numpy as np

def readNames():
	with open('p098_words.txt', 'r') as file:
		data = file.read().replace('"','')
		return data.split(',')

def findAnagrams(n):
	words_characters = {}
	anagrams = []
	for word in words[n]:
		characters = {}
		for c in word:
			if c in characters:
				characters[c] += 1
			else:
				characters[c] = 1
		for w,c in words_characters.items():
			if characters == c:
				anagrams.append([w,word])
		words_characters[word] = characters
	return anagrams

def get_squares(n):
	n_min = int(np.sqrt(10**(n-1))) + 1
	n_max = int(np.sqrt(10**n))
	s = []
	for n in range(n_min,n_max):
		s.append(n**2)
	return s

def find_square_anagrams(a):
	square_ana_list = []
	for square in squares:
		char_digit = {}
		square = str(square)
		possible_square_found = False
		available_digits = list(range(0,10))
		for idx, c in enumerate(a[0]):
			d = int(square[idx])
			if c in char_digit:
				if char_digit[c] != d:
					break
			else:
				if d not in available_digits:
					break
				else:
					char_digit[c] = d
					available_digits.remove(d)
			if idx == len(a[0])-1:
				possible_square_found = True
		
		if possible_square_found:
			n = ''
			for c in a[1]:
				n = n + str(char_digit[c])
			n = int(n)
			if n in squares:
				square_ana_list += [int(square),n]
	return square_ana_list

start = timer()
words = {}
for w in readNames():
	l = len(w)
	if l < 4:
		continue
	if l in words:
		words[l].append(w)
	else:
		words[l] = [w]

n = 13
while True:
	square_anas = []
	anagrams = findAnagrams(n)
	squares = get_squares(n)
	for a in anagrams:
		square_ana_list = find_square_anagrams(a)
		square_anas += square_ana_list
	if square_anas:
		break
	n-=1

end = timer()
print('Largest square anagrams: {}'.format(square_anas))
print('Time elapsed: {}'.format(end-start))


