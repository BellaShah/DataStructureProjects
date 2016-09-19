
#  File: TestSparseMatrix.py

#  Description: Sparse matrix representation has a single linked 
#  list having the row, column, and non-zero data in each link

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: April 11, 2016

#  Date Last Modified: April 13, 2016

class Link (object):
  def __init__ (self, row = 0, col = 0, data = 0, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = next

  # returns a String representation
  def __str__ (self):
    s = '(' + str(self.row) + ', ' + str(self.col) + ', ' + str(self.data) + ')'
    return s

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertLast (self, row, col, data):
    newLink = Link (row, col, data)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  def __str__ (self):
    current = self.first
    s = str(current)
    current = current.next
    while current != None:
      s += ', ' + str(current)
      current = current.next
    return s

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = LinkedList()
  # setElement() perform an assignment operation a[i][j] = value
  # if value is 0 the link if it exists is deleted
  # if value is non zero then the current value is updated if a
  # link already exists or a new link is added
  def setElement (self, row, col, data):
    
    previous = self.matrix.first
    current = self.matrix.first
    
    while current != None:
      if current.row == row and current.col == col:
        if data == 0:
          if current.next == None:
            previous.next == None
          if current == self.matrix.first:
            self.matrix.first = current.next
          previous.next = current.next
          return    
        current.data = data
        return
        
      if (current.col == col and current.row > row) or current.col > col:
        if data == 0:
          return  
        newLink = Link(row, col, data)
        previous.next = newLink
        newLink.next = current
        return
        
      previous = current
      current = current.next
      

  def insertLink (self, row, col, data):
    # do nothing if data = 0
    if (data == 0):
      return

    # create a new link
    newLink = Link (row, col, data)

    # if matrix is empty then the newLink is the first link
    if (self.matrix == None):
      self.matrix = newLink
      return

    # find position to insert
    previous = self.matrix
    current = self.matrix

    while ((current != None) and (current.row < row)):
      previous = current
      current = current.next

    # if the row is missing
    if ((current != None) and (current.row > row)):
      previous.next = newLink
      newLink.next = current
      return
  
    # on the row, search by column
    while ((current != None) and (current.col < col)):
      previous = current
      current = current.next

    # if link already there do not insert but reset data
    if ((current != None) and (current.row == row) and (current.col == col)):
      current.data = data
      return

    # now insert newLink
    previous.next = newLink
    newLink.next = current


  # deletes and returns a Link if it is there or None otherwise
  def deleteLink (self, row, col):
    current = self.matrix.first
    previous = self.matrix.first
    while current != None:
      if current.col == col and current.row == row:
        if current == self.matrix.first:
          self.matrix.first = self.matrix.first.next
        else:
          previous.next = current.next
        return current
      else:
        previous = current
        current = current.next
    return None
      
  # add two sparse matrices 
  def __add__ (self, other):
    if self.row != other.row or self.col != other.col:
      return None
      
    matrix_add = Matrix(self.row, self.col)
    for i in range(self.row):
      for j in range(self.col):
        matrix_add.matrix.insertLast(i, j, self.getRow(i)[j] + other.getRow(i)[j])      
      
    return matrix_add


  # multiply two sparse matrices 
  def __mul__ (self, other):
    if self.col != other.row:
      return None
      
    matrix_multiply = Matrix(self.row, other.col)
    for i in range(self.row):
      for j in range(other.col):
        sum = 0
        for k in range(self.col):
          sum += self.getRow(i)[k] * other.getCol(j)[k]
        matrix_multiply.matrix.insertLast(i, j, sum)
        
    return matrix_multiply


  # return a row of the sparse matrix
  def getRow (self, n):
    current = self.matrix.first
    row = self.col * [0]
    
    while current != None:
      if current.row == n:
        row[current.col] = current.data
      current = current.next
      
    return row

  # return a column of the sparse matrix
  def getCol (self, n):
    current = self.matrix.first
    col = self.row * [0]
    
    while current != None:
      if current.col == n:
        col[current.row] = current.data
      current = current.next
      
    return col

  # return a string representation of a matrix
  def __str__ (self):
    s = ''
    for i in range(self.row):
      this_row = self.getRow(i)
      s += str(this_row[0]).rjust(2) 
      for j in range(1, self.col):
        s += str(this_row[j]).rjust(3) 
      s += '\n'
    return s
  
def readMatrix (inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  # Add each element from inFile into the Matrix for mat
  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      elt = int(line[j])
      if (elt != 0):
        mat.matrix.insertLast (i, j, elt)
  line = inFile.readline()

  return mat

def main ():
  inFile = open ("matrix.txt", "r")

  print ("\nTest Matrix Addition")
  matA = readMatrix (inFile)
  print (matA)
  matB = readMatrix (inFile)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)
  
  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.setElement (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Element to Zero")
  matA.setElement (1, 1, 0)
  print (matA)

  print ("\nTest Getting a Row")
  row = matP.getRow(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.getCol(0)
  print (col)

  inFile.close()

main()