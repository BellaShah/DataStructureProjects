#  File: Work.py

#  Description: This program outputs the number of lines Vyasa has to write based on his productivity factor. 

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: March 26, 2016

#  Date Last Modified: March 26, 2016

# Finds the number of lines
# v - first lines of code
# k - productivity factor
def num_lines(v, k, factor):
	counter = 0
	Vyasa_Code = 0
	v -= 1
	while True:
		Vyasa_Code += (v // factor ** counter)
		
		if (Vyasa_Code >= k):
			return 1

		elif(Vyasa_Code < k) and ((v // factor ** (counter + 1)) == 0):
			return 2
		counter += 1

# Finds the number of lines in sequence 
def Sequence(v, k, factor):
	counter = 0
	Vyasa_Code = 0

	while True:
		Vyasa_Code += (v // factor ** counter)
		if (Vyasa_Code > k):
			return num_lines(v, k, factor)
		elif (Vyasa_Code == k) and ((v // factor ** (counter + 1)) == 0):
			return 2
		elif (Vyasa_Code < k) and ((v // factor ** (counter + 1)) == 0):
			return 3
		counter += 1

# Binary search to find the number of lines of code student must begin assigment with
def binSearch(k, factor):
	lo = 0
	hi = k

	while lo <= hi:
		v = (lo + hi) // 2

		target = Sequence(v, k, factor)
		if target == 2:
			return v
		elif target == 1:
			hi = v - 1
		elif target ==  3:
			lo = v + 1

def main():

	inFile = open ("work.txt", "r")
	numLines = int(inFile.readline().rstrip("\n"))

	# Reads in each line and print the optimal lines code to write
	for i in range(numLines):
		prnt_lne = inFile.readline().rstrip("\n").split()
		print(str(binSearch(int(prnt_lne[0]),int(prnt_lne[1]))))

	# Closes file
	inFile.close()

main()