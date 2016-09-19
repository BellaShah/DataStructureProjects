#  File: Nim.py

#  Description: This program is a simulation of the Nim Sum game. The program find the first move to win a game of Nim Sum. 

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: January 30, 2015

#  Date Last Modified:January 30, 2015

# Computes the NimSum of all of the heaps
def TotalNimSum(heaps):
  NimSum = heaps[0]
  for i in range (1, len(heaps)):
    NimSum = NimSum ^ heaps[i]
  return NimSum 

# Computes the nimsum with each individual heap 
def IndvlNimSum(heaps): 
  for pile in range (len(heaps)):
        heapNimSum = heaps[pile]^TotalNimSum(heaps) # Nim-sum for each individual heap
        if(heapNimSum < heaps[pile]):
          counters = heaps[pile] - heapNimSum
          print("Remove", counters, "counters from Heap", pile + 1) # Prints result
          break    
def main():

  # Opens and reads nim.txt file
  Nim_File = open("nim.txt", "r")

  # Reads the first line of nim.txt which is the number of games to play
  numGames = int(Nim_File.readline())

  # Runs each game
  for game in range (0,numGames):
    Heap = Nim_File.readline().split()  
    List_heaps = [int(c) for c in Heap] # Creates a list of each heap as an integer and the number of counters per heap
    nimSum = TotalNimSum(List_heaps) # Calls function to find total nim sum
    
    # Checks the Nim Sum, if 0, the player cannot win, if not 0, it computes the individual nim sum
    if(nimSum == 0):
      print("Lose Game")
    else:
      IndvlNimSum(List_heaps) # Calls function to compute nim sum of each individual heap

  # Closes nim.txt file      
  Nim_File.close()

main()