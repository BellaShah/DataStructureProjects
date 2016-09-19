#  File: TestLinkedList.py

#  Description: This program tests a linked list class and test cases.

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: April 2, 2016

#  Date Last Modified: April 2, 2016

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
    
  def __str__(self):
    return str(self.data)
    
class LinkedList (object):

  def __init__ (self):
    self.first = None

  # get number of links 
  def getNumLinks (self):
    count = 0
    current = self.first
    
    while current != None:
      count += 1
      current = current.next
      
    return count
    
  # Add data at the beginning of the list
  def addFirst (self, data): 
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  # Add data at the end of a list
  def addLast (self, data): 
    newLink = Link (data)
    current = self.first

    if self.isEmpty():
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink
    
  # Add data in an ordered list in ascending order
  def addInOrder (self, data): 
    newLink = Link (data)
    previous = self.first
    current = self.first
    
    if self.isEmpty():
      self.first = newLink
      return
  
    while (current.data <= data):
      if current.next == None:
        current.next = newLink
        return
      else:
        previous = current
        current = current.next
    
    if current == self.first:
      self.addFirst(data)
      return
      
    previous.next = newLink
    newLink.next = current

  # Search in an unordered list, return None if not found
  def findUnordered (self, data): 
    current = self.first
    if self.isEmpty():
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current
    
  # Search in an ordered list, return None if not found
  def findOrdered (self, data): 
    current = self.first
    if self.isEmpty():
      return None
      
    while (current.data != data):
      if (current.next == None):
        return None
      elif (current.next.data > data):
        return None
      else:
        current = current.next
        
    return current
    
  # Delete and return Link from an unordered list or None if not found
  def delete (self, data):
    current = self.first
    previous = self.first

    if self.isEmpty():
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    string = '['
    current = self.first
    totalItems = 1
    
    if self.isEmpty():
      return '[]'
    
    for i in range(self.getNumLinks() - 1):
      string += str(current.data) + '  '
      current = current.next
      totalItems += 1
      if (totalItems - 1) % 10 == 0:
        string += '\n '
    
    string += str(current.data) + ']'
    return string

  # Copy the contents of a list and return new list
  def copyList (self):
    copy = LinkedList()
    current = self.first
    
    while (current != None):
      copy.addLast(current.data)
      current = current.next
      
    return copy

  # Reverse the contents of a list and return new list
  def reverseList (self): 
    current = self.first
    
    if self.isEmpty():
      return self
      
    isReversed = LinkedList()
    for i in range(self.getNumLinks()):
      isReversed.addFirst(current.data)
      current = current.next
      
    return isReversed
    
  # Sort the contents of a list in ascending order and return new list
  def sortList (self): 
    sortedLinked = LinkedList()
    if self.isEmpty():
      return sortedLinked
    
    current = self.first
    for i in range(self.getNumLinks()):
      sortedLinked.addInOrder(current.data)
      current = current.next  
      
    return sortedLinked
    
  # Return True if a list is sorted in ascending order or False otherwise
  def isSorted (self):
    current = self.first
    if self.isEmpty() or self.getNumLinks() == 1:
      return True
      
    for i in range(self.getNumLinks() - 1):
      if current.data > current.next.data:
        return False
      current = current.next
      
    return True 

  # Return True if a list is empty or False otherwise
  def isEmpty (self): 
    return (self.first == None)

  # Merge two sorted lists and return new list in ascending order
  def mergeList (self, b):
    current = b.first
    merged = self.copyList().sortList()
    
    if self.isEmpty():
      if b.isEmpty():
        return merged
      else:
        merged = b.copyList()
        return merged
    elif b.isEmpty():
      return merged
  
    for i in range(0,b.getNumLinks()):
      merged.addInOrder(current.data)
      current = current.next
      
    return merged
        
  # Test if two lists are equal, item by item and return True
  def isEqual (self, b):
    if self.getNumLinks() != b.getNumLinks():
      return False
      
    if self.isEmpty() and b.isEmpty():
      return True
      
    current_frst = self.first
    current_snd = b.first
    
    for i in range(self.getNumLinks()):
      if current_frst.data != current_snd.data:
        return False
      current_frst = current_frst.next
      current_snd = current_snd.next
      
    return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def removeDuplicates (self):
    removed = self.copyList()
    previous = removed.first
    current = removed.first
    Indv_Elmnts = []   # List of unique elements

    for i in range(removed.getNumLinks()):
      if current.data in Indv_Elmnts:
        current = current.next
        previous.next = current
      else:
        Indv_Elmnts.append(current.data)
        previous = current
        current = current.next
        
    return removed

def main():

  # Test methods addFirst() and __str__() by adding more than
  # 10 items to a list and printing it.
  print()
  print("Test addFirst() and __str__():")
  
  theList = LinkedList()
  theList.addFirst(6)
  theList.addFirst(10)
  theList.addFirst(5)
  theList.addFirst(3)
  theList.addFirst(15)
  theList.addFirst(2)
  theList.addFirst(1)
  theList.addFirst(14)
  theList.addFirst(7)
  theList.addFirst(8)
  theList.addFirst(12)
  theList.addFirst(9)
  theList.addFirst(11)
  theList.addFirst(4)
  theList.addFirst(13)
  
  print(theList)
  
  # Test method addLast()
  print()
  print("Test addLast():")
  theList2 = LinkedList()
  theList.addLast(6)
  theList.addLast(10)
  theList.addLast(5)
  theList.addLast(3)
  theList.addFirst(15)
  theList.addFirst(2)
  theList.addFirst(1)
  theList.addFirst(14)
  theList.addFirst(7)
  theList.addFirst(8)
  theList.addFirst(12)
  theList.addFirst(9)
  theList.addFirst(11)
  theList.addFirst(4)
  theList.addFirst(13)
  
  print(theList)

  # Test method addInOrder()
  print()
  print("Test addInOrder():")
  
  sortedList = theList.sortList()
  sortedList.addInOrder(9)
  sortedList.addInOrder(6)
  sortedList.addInOrder(3)
  sortedList.addInOrder(71)

  print(sortedList)
  
  # Test method getNumLinks()
  print()
  print("Test getNumLinks():")
  print(theList.getNumLinks())  

  # Test method findUnordered() 
  # Consider two cases - item is there, item is not there
  print()
  print("Test findUnordered():") 
  
  there = theList.findUnordered(14)
  print(there)
  
  not_there = theList.findUnordered("I love CS")
  print(not_there)

  not_there = theList.findUnordered(5000)
  print(not_there)
  
  # Test method findOrdered() 
  # Consider two cases - item is there, item is not there 
  print()
  print("Test findOrdered()")
  
  there = sortedList.findOrdered(17)
  print(there)
  
  not_there = sortedList.findOrdered(949)
  print(not_there)

  # Test method delete()
  # Consider two cases - item is there, item is not there 
  print()
  print("Test delete():")
  newList = sortedList.copyList()
  there = newList.delete(7)
  print(newList)
  print("Deleted Link:", there.data)
  
  print()
  newList = theList.copyList()
  not_there = newList.delete(100)
  print(newList)
  print("Deleted Link:", not_there)

  # Test method copyList()
  print()
  print("Test copyList():")
  copy = theList.copyList()
  print(copy)
  
  sortedCopy = sortedList.copyList()
  print(sortedCopy)

  # Test method reverseList()
  print()
  print("Test reverseList():")
  reverseTest = sortedList.reverseList()
  print(reverseTest)
  print(reverseTest.reverseList())
  
  # Test method sortList()
  print()
  print("Test sortList()")
  sortedList = theList.sortList()
  print(sortedList)

  # Test method isSorted()
  # Consider two cases - list is sorted, list is not sorted
  print()
  print("Test isSorted():")
  print(theList.isSorted())
  print(sortedList.isSorted())

  # Test method isEmpty()
  print()
  print("Testing method isEmpty():")
  print(theList.isEmpty())
  
  emptyList = LinkedList()
  print(emptyList.isEmpty())
  
  # Test method mergeList()
  # Create new sorted lists to test method on
  print()
  print("Testing mergeList():")
  List1 = LinkedList()
  for i in range (1, 14, 2):
    List1.addLast(i)

  List2 = LinkedList()
  for j in range(2, 15, 2):
    List2.addLast(j)
    
  mergeSort = List1.mergeList(List2)
  print("List 1:", List1)
  print("List 2:", List2)
  print("Merged List:", mergeSort)

  # Test method isEqual()
  # Consider two cases - lists are equal, lists are not equal
  print()
  print("Test isEqual():")
  print(theList.isEqual(sortedList))
  print(theList.isEqual(copy))

  # Test removeDuplicates()
  print()
  print("Test removeDuplicates()")
  removedSorted = sortedList.removeDuplicates()
  print(removedSorted)
  
main()