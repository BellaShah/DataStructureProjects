class EightQueens (object):
  # Initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    self.numSolutions = 0
    
    # Populate chess board with '*' before adding queens
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # Check if a queen can be placed in row and col without being 
  #   captured by another queen currently on the board
  def isValid (self, row, col):
    
    # Check horizontal and vertical paths
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    
    # Check diagonal paths
    for i in range (self.n):
      for j in range (self.n):
        rowDiff = abs (row - i)
        colDiff = abs (col - j)
        if (rowDiff == colDiff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # Find all possible solutions 
  def recursiveSolve (self, col):
    if (col == self.n):
      self.printBoard()
      print()
      self.numSolutions += 1
    else:
      # Check each row in current col to see if a Queen can be put there.
      #   When each possible queen placement is found, there is a recursive
      #   call to finish the possible solutions with the given queen placement.
      for i in range (self.n):
        if (self.isValid (i, col)):
          self.board[i][col] = 'Q'
          self.recursiveSolve (col + 1)
          self.board[i][col] = '*'

  # Initiate the solve function and print the number of solutions
  def solve (self):
    self.recursiveSolve (0)
    self.printNumSolutions()

  # Print each board
  def printBoard (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ' )
      print ()
      
  def printNumSolutions(self):
    print("There are", self.numSolutions, "solutions for a", 
    	  self.n, "x", self.n, "board.\n")
  
  
def main():

  print() 
  
  # Get board size from user
  validInput = False
  while not validInput:
    try:
      size = eval(input("Enter the size of the board: "))
      validInput = True
    except:
      validInput = False
  while size not in [1,2,3,4,5,6,7,8]:
    size = eval(input("Enter an integer in the range 1 to 8: "))
	
  print()
  
  queens = EightQueens (size)
  queens.solve()


main()