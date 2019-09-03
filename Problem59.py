'''

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). 
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. 
Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, 
and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

'''


def readFile():
	with open('p059_cipher.txt','r') as f:
		data = f.read()
		s = data.split(',')
		return [int(x) for x in s]

def decypher(asc):
	for i in range(97,123):
		for j in range(97,123):
			for k in range(97,123):
				asc_de = []
				counter = 0
				for a in asc:
					c = counter % 3
					if c == 0:
						asc_de.append(a^i)
					elif c == 1:
						asc_de.append(a^j)
					else:
						asc_de.append(a^k)
					counter += 1
				if search(asc_de):
					return asc_de

def search(asc_de):
	s = [chr(x) for x in asc_de]
	for i,c in enumerate(s):
		if s[i] == 't' and s[i+1] == 'a' and s[i+2] == 'k' and s[i++3] == 'e' and s[i+4] == 'n':
			print(''.join(s))
			return True
	return False


if __name__ == '__main__':
	asc = readFile()
	asc_de = decypher(asc)
	print(sum(asc_de))
	




