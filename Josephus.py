#  File: Josephus.py

#  Description: This program solves Josephus' problem using a circular linked list. 

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: April 9, 2016

#  Date Last Modified: April 9, 2016

class Link(object):
	# Constructor
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class CircularList(object):
	# Constructor
	def __init__ (self):
		self.first = None

	# Insert an element in the list
	def insert (self, item):
		newLink = Link(item)

		if self.first == None:
			self.first = newLink
			newLink.next = self.first
			self.first = newLink
			return
		current = self.first
		while current.next != self.first:
			current = current.next

		current.next = newLink
		newLink.next = self.first
		newLink.previous = current
	
	# Find the link with the given key
	def find (self, key):
		current = self.last
		while current.data != key:
			current = current.next
			
		return current

	# Delete a link with a given key
	def delete (self, key):
		if self.first == None:
			return None

		current = self.first
		previous = self.first

		while previous.next != self.first:
			previous = previous.next

		while current.data != key:
			
			if current.next == self.first:
				return None

			previous = current
			current = current.next

		if current == self.first:
			if self.first == self.first.next:
				self.first = None
				return current
			else:
				self.first = current.next

		previous.next = current.next

		return current

  	# Delete the nth link starting from the Link start 
  	# Return the next link from the deleted Link
	def deleteAfter (self, start, n):
		if self.first == None:
			return None
		
		current = self.first
		while (current.data != start):
			current = current.next
		
		count = 1
		while (count != n):
			current = current.next
			count += 1
	 
		self.delete(current.data)
		print(current.data, end = " ")
		return current.next

	# Return a string representation of a Circular List	
	def __str__(self):
		string = '['
		current = self.last.next
		numItems = 0
		if current == self.last:
			string += str(current.data) + ']'
			return string
		while True:
			string += str(current.data) + '  '
			current = current.next
			numItems += 1
		string += str(current.data) + ']'
		return string

def main():

	inFile = open("./Josephus.txt", "r")
	numSoldiers = eval(inFile.readline().strip())
	start = int(inFile.readline().strip())
	skip = eval(inFile.readline().strip())

	inFile.close()

	list_soldiers = CircularList()

	for i in range(1, numSoldiers + 1):
		list_soldiers.insert(i)

	for i in range(numSoldiers):
		start = list_soldiers.deleteAfter(start, skip)
		start = start.data
main()