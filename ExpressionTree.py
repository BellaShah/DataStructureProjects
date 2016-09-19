#  File: ExpressionTree.py

#  Description: Creates an expression tree to evaluate post-fix and pre-fix operations of Polish notation. 

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: April 23, 2016

#  Date Last Modified: April 23, 2016

def main():
  with open("expression.txt") as inFile:
    #Reads each line if more than one line and prints results
    for line in inFile: 
      tree = Tree()
      tree.createTree(line)
      print()
      # Print results
      print(line, '=' , int(tree.evaluate(tree.root)))
  
      # Print results
      print("Prefix Expression:", end = ' ') 
      tree.preOrder(tree.root)
      print()
      print("Postfix Expression:", end = ' ')
      tree.postOrder(tree.root)
      print()

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = Node(None)    

  def createTree (self, line):
    notation = line.split()
    parents = Stack()	
    current = self.root
    
    for symbl in notation:
      if symbl == '(':
        parents.push(current)
        current.lChild = Node(None)
        current = current.lChild
        
      elif symbl in ['+', '-', '*', '/']:
        current.data = symbl
        parents.push(current)
        current.rChild = Node(None)
        current = current.rChild
        
      elif symbl.isdigit() or '.' in symbl:
        current.data = symbl
        current = parents.pop()
        
      elif symbl == ')':
        if not parents.isEmpty():
          current = parents.pop()
        else:
          break

  def evaluate (self, aNode):  
    if aNode.data == '+':
      return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
    elif aNode.data == '-':
      return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild) 
    elif aNode.data == '*':
      return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
    elif aNode.data == '/':
      return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
      
    elif aNode.data.isdigit() or '.' in aNode.data:
      return eval(aNode.data)
  
# pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print(aNode.data, end = ' ')
      self.preOrder (aNode.lChild)
      self.preOrder (aNode.rChild)

  # post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lChild)
      self.postOrder (aNode.rChild)
      print(aNode.data, end = ' ')

main()