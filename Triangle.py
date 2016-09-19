#  File: Triangle.py

#  Description: Finds the greatest path sum of a triangle 

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: April 16, 2016

#  Date Last Modified: April 16, 2016

# returns the greatest path sum using exhaustive search
def exhaustive_search (triangle):
  return exhaustive_search2(triangle )

def exhaustive_search2(triangle , row = 0, col = 0, total = 0):
  if row == len(triangle ):
    return total
  total = total + triangle [row][col]
  return max(exhaustive_search2(triangle ,row + 1, col, total), exhaustive_search2(triangle , row + 1, col + 1,total))

# returns the greatest path sum using greedy approach
def greedy (triangle):
  return greedy2(triangle , total = triangle [0][0])

def greedy2(triangle , row = 0, col = 0, total = 0):
  if row == len(triangle ) - 1:
    return total
  if triangle [row+1][col] > triangle [row+1][col+1]:
    max_col = col
  else:
    max_col = col+1
  total = total + triangle [row + 1][max_col]
  
  return greedy2(triangle , row + 1, max_col, total)

# returns the greatest path sum using divide and conquer (recursive) approach
def recursivegrid(triangle):
  return rec_search(triangle , len(triangle )-2)
def rec_search (rowData, rowNum):
    for i in range(len(rowData[rowNum])):
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    if len(rowData[rowNum])==1: 
      return rowData[rowNum][0]
    else: 
      return rec_search(rowData, rowNum-1)

# returns the greatest path sum using dynamic programming
def dynamic_prog (triangle):
  return dynamic_prog2(triangle , len(triangle )-1)

def dynamic_prog2(triangle , row, grid = []):
  if row == -1:
    return grid[0][0]
  elif row == len(triangle )-1:
    grid.insert(0,triangle [row])
  else:
    new_row = []
    for i in range(len(triangle [row])):
      new_row.append(triangle [row][i]+max(grid[0][i],grid[0][i+1]))
    grid.insert(0, new_row)

  return dynamic_prog2(triangle , row-1, grid)

# reads the file and returns a 2-D list that represents the triangle
def readGrid():
  matrix = []
  inFile = open ("triangle.txt", "r")
  num_rows = int(inFile.readline().rstrip("\n"))
  for i in range(num_rows):
    row = inFile.readline().rstrip("\n").split()
    for k in range(len(row)):
      row[k] = int(row[k])
    matrix.append(row)
  inFile.close()
  return matrix

def main ():
  # read triangular grid from file
  matrix = readGrid()
  rec_matrix = readGrid()

  # output greates path from exhaustive search
  print ('The greatest path sum through exhaustive search is ' + str(exhaustive_search(matrix)) + '.')
  
  # output greates path from greedy approach
  print ('The greatest path sum through greedy search is ' + str(greedy(matrix)) + '.')

  # output greates path from divide-and-conquer approach
  print ('The greatest path sum through recursive search ' + str(recursivegrid(rec_matrix)) + '.')

  # output greates path from dynamic programming 
  print ('The greatest path sum through dynamic programming is ' + str(dynamic_prog(matrix)) + '.')

main()