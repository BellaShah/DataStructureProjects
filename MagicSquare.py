#  File: MagicSquare.py

#  Description: This program will generate a magic sqaure from an odd number and find the sum of the row, column and diagonal.

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: February 5, 2016

#  Date Last Modified: February 5, 2016

# Make a magic square of the size prompted by user in main method
def makeSquare(n):

	# Create magic square
	square = []
	for i in range(n):
		row = []
		for j in range(n):
			row.append(0)
		square.append(row)
	
	# Position first number in the middle of square
	row = n - 1
	col = n // 2
	square[row][col] = 1
	
	# Method to populate square by finding spot diagonally down and to the right.
	# If space is occupied, the number goes directly above the first number. 
	for k in range(1, n*n):
		
		if (row + 1 == n) and (col + 1 == n):
			row -= 1
			square[row][col] = k + 1

		else:
			tempRow = (row + 1) % n
			tempCol = (col + 1) % n
			
			if square[tempRow][tempCol] == 0:
				row = tempRow
				col = tempCol
				square[row][col] = k + 1
			else:
				row -= 1
				square[row][col] = k + 1
			
	checkSquare(square)

# Print the magic square in a neat format where the numbers are right justified
def printSquare(magicSquare):

	maximum = len(str(magicSquare[0][len(magicSquare) // 2]))
	for row in magicSquare:
		for num in row:
			print(" "*(maximum-len(str(num)))+str(num),end = " ")
		print()

# Checks that the 2-D list generated is indeed a magic square
# Prints the sum of the row, column, RL and LR diagonals 
def checkSquare(magicSquare):

	isMagic = True
	n = len(magicSquare)
	expectedSum = n * (n**2 + 1) / 2
	
	
	# Check the sums of the numbers from the upper right to lower left
	sum_rl = 0
	column = 0
	for i in range(n):
		sum_rl += magicSquare[i][column]
		column += 1
	if sum_rl != expectedSum:
		isMagic = False
		
	# Check the sums of the numbers from the upper left to lower right
	sum_lr = 0
	row = n - 1
	for i in range(n):
		sum_lr += magicSquare[row][i]
		row -= 1
	if sum_lr != expectedSum:
		isMagic = False	
		
	# Check the sums of the numbers in each row
	for i in range(n):
		sum_row = 0
		for j in range(n):
			sum_row += magicSquare[i][j]
		if sum_row != expectedSum:
			isMagic = False

			
	# Check the sums of the numbers in each column 
	for i in range(n):
		sum_column = 0
		for j in range(n):
			sum_column += magicSquare[j][i]
		if sum_column != expectedSum:
			isMagic = False
				
	# Prints the magic square and sum of row, column and diagonals
	if isMagic:
		printSquare(magicSquare)
		print()
		print("Sum of row =", sum_row)
		print("Sum of column =" , sum_column)
		print("Sum diagonal (UL to LR) =" , sum_lr)
		print("Sum diagonal (UR to LL) =" , sum_rl)
	
def main():

	# Prompts user for desired  odd number dimension of magic square
	# If size is not greater than 3 or an odd number, it prompts the user again 
	size = int(input("\nPlease enter an odd number: "))
	while (size%2 == 0 or size<3):
		size = int(input("\nPlease enter an odd number: "))

	# Prints the magic square
	print("\nHere is a ", str(size), "x", str(size), "magic square: \n")	
	makeSquare(size)

main()