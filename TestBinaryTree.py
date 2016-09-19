#  File: TestBinaryTree.py

#  Description: Creates an Binary Search Tree and tests several function. Also, created test cases.  

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: April 26, 2016

#  Date Last Modified: April 26, 2016

import random

def main():
  
  # Create three trees - two are the same and the third is different
  # Tree_ A, Tree_B are the same and Tree_C is different and random
  tree_A = Tree()
  tree_A.insert(11)
  tree_A.insert(7)
  tree_A.insert(77)
  tree_A.insert(15)
  tree_A.insert(87)
  tree_A.insert(92)
  tree_A.insert(1)
  tree_A.insert(93)
  tree_A.insert(45)
  tree_A.insert(37)
  tree_A.insert(12)
  tree_A.insert(99)
  tree_A.insert(4)
  tree_A.insert(10)
  tree_A.insert(51)
  
  tree_B = Tree()
  tree_B.insert(11)
  tree_B.insert(7)
  tree_B.insert(77)
  tree_B.insert(15)
  tree_B.insert(87)
  tree_B.insert(92)
  tree_B.insert(1)
  tree_B.insert(93)
  tree_B.insert(45)
  tree_B.insert(37)
  tree_B.insert(12)
  tree_B.insert(99)
  tree_B.insert(4)
  tree_B.insert(10)
  tree_B.insert(51)
  
  
  tree_C = Tree()
  numOfNodes = random.randint(16, 30)
  for i in range(numOfNodes):  
    tree_C.insert(random.randint(1,99))
  
  # Test your method isSimilar()
  print("\ntree1 and tree_B are similar: ", tree_A.isSimilar(tree_B))
  print("tree_B and tree_C are similar: ", tree_B.isSimilar(tree_C))
  
  
# Print the various levels of two of the trees that are different
  print("\nThe levels of tree_A are:")
  for levelA in range(1, 16):
    tree_A.printLevel(levelA)
    
  print("\nThe levels of tree_C are:")
  for levelC in range(1,tree_C.getHeight()+1):
    tree_C.printLevel(levelC)
    
  # Get the height of the two trees that are different
  print("\nThe height of tree_A is: ", tree_A.getHeight())

  # Makes sure tree heights are different, otherwise adds node to tree_C.
  while(tree_A.getHeight() == tree_C.getHeight()): 
      tree_C.insert(random.randint(1,99))

  print("The height of tree_C is: ", tree_C.getHeight())
    
  # Get the number of nodes in the left and right subtree
  print("The number of nodes in tree_B is: ", tree_B.numNodes())
  print("The number of nodes in tree_C is: ", tree_C.numNodes())

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # Inserts a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

   # Returns true if two binary trees are similar
  def isSimilar(self, other):
    node1 = self.root
    node2 = other.root
    return self.comparison(node1, node2)
  
  # Helper function for isSimiliar
  def comparison(self, node1, node2):
    if node1 == None and node2 == None:
      return True
      
    if node1 == None and node2 != None:
      return False
    elif node1 != None and node2 == None:
      return False
    elif node1.data != node2.data:
      return False
    else:
      return self.comparison(node1.lChild, node2.lChild) and self.comparison(node1.rChild, node2.rChild)
    
  # Prints out all nodes at the given level
  def printLevel(self, level):
    nodes = []
    self.helper_Level(level, 1, nodes, self.root)
    if len(nodes) == 0:
      return 
    else:
      print(nodes)
    
  # Helper for printLevel
  def helper_Level(self, level, currentLevel, nodes, oneNode):
    if currentLevel > level:
      return
    
    if oneNode == None:
      return
    else:
      if currentLevel == level:
        nodes.append(oneNode.data)
      else:
        self.helper_Level(level, currentLevel + 1, nodes, oneNode.lChild)
        self.helper_Level(level, currentLevel + 1, nodes, oneNode.rChild)
    

  # Returns the height of the tree
  def getHeight(self):
    tree_height = [0]
    self.heightCount(self.root, 0, tree_height)
    tree_height.sort()
    return tree_height[-1]   
    
  # Helper for getHeight
  # Traverses tree and finds the length for all possible paths from root to leaf
  def heightCount(self, oneNode, tree_size, tree_height):
    if oneNode == None:
      tree_height.append(tree_size)
    else:
      tree_size += 1
      self.heightCount(oneNode.lChild, tree_size, tree_height)
      self.heightCount(oneNode.rChild, tree_size, tree_height)
          
  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree
  def numNodes(self):
    nodes = self.nodeCount(self.root)
    return nodes
    
  # Keeps count of the number of nodes 
  def nodeCount(self, oneNode):
    if oneNode == None:
      return 0
    else:
      return 1 + self.nodeCount(oneNode.lChild) + self.nodeCount(oneNode.rChild)
       
main()