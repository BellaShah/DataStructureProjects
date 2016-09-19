#  File: TestCipher.py

#  Description: This program converts a message that we are asked to encode or decode to lower case.

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: March 26, 2016

#  Date Last Modified: March 28, 2016

# Creates the plain and cipher text as global variables so that it can be accessed by all functions
plain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipher = [ 'q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']

def vigenere_decode (phrase, password):
	decodedWord = " "
	passwdIter = 0
	
	for i in range(len(phrase)):
		if phrase[i].isalpha():
			decodedWord += decryption(phrase[i], password[passwdIter])
			passwdIter += 1 
			if passwdIter == len(password):
				passwdIter = 0
		else:
			decodedWord += phrase[i] # Concatnates string 
	return decodedWord

def vigenere_encode (phrase, password):
	encodedWord = " "
	passwdIter = 0
	
	for i in range(len(phrase)):
		if phrase[i].isalpha():
			encodedWord +=  encryption(phrase[i], password[passwdIter])
			passwdIter += 1 
			if passwdIter == len(password):
				passwdIter = 0
		else:
			encodedWord += phrase[i] # Concatnates string 
	return encodedWord

def substitution_decode(phrase):
	regularText = []
	for char in phrase:
		if char == ' ':
			regularText.append(' ')
		elif not ('a' <= char <= 'z'):
			regularText.append(char)
		else:
			idx = cipher.index(char)
			regularText.append(plain[idx])

	# Converts the normal text into a string 
	return (''.join(regularText))

def substitution_encode(phrase):
	encrypted_text = []
	for char in phrase:
		if char == ' ':
			encrypted_text.append(' ')
		elif not ('a' <= char <= 'z'):
			encrypted_text.append(char)
		else:
			idx = ord(char) - ord('a')
			encrypted_text.append(cipher[idx])

	# Converts the "coded word" into a string
	return (''.join(encrypted_text))

# Function to encrypt text for vigenere
def encryption( symbol , password ):
	symbol_idx = (ord(symbol)-97)
	password_idx = (ord(password)-97)
	character_cryption = (symbol_idx + password_idx) % 26
	
	return chr(ord('a') + character_cryption)

# Function to decrypt text for vigenere
def decryption( symbol , password  ):
	symbol_idx = (ord(symbol)-97)
	password_idx = (ord(password)-97)
	character_cryption = (symbol_idx - password_idx) % 26

	return chr(ord('a') + character_cryption)

def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (line.lower())

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (line.lower())

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  password = in_file.readline()
  password = password.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line.lower(), password.lower())

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + password)
  print ("Encoded Text:" + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  password = in_file.readline()
  password = password.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line.lower(), password.lower())

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + password)
  print ("Decoded Plain Text:" + decoded_str)
  print ()

  # close file
  in_file.close()

main()