#  File: Mondrian.py

#  Description: This program will recreate Mondrian's paintings

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: March 5, 2016

#  Date Last Modified: March 6, 2016
from tkinter import *
import turtle
import random

# Function draws the lines in a box shape
def Square(ttl, color, x_1, y_1, x_2, y_2):
	ttl.color('black', color)
	ttl.penup()
	ttl.goto(x_1, y_1)
	ttl.begin_fill()
	ttl.pendown()
	ttl.goto(x_1, y_2)
	ttl.goto(x_2, y_2)
	ttl.goto(x_2, y_1)
	ttl.goto(x_1, y_1)
	ttl.end_fill()
	ttl.color('black')

# Function physically draws the lines
def Line(ttl, x1, y1, x2, y2):
	ttl.penup()
	ttl.goto(x1, y1)
	ttl.pendown()
	ttl.goto(x2, y2)

# Function randomly chooses the path of the horizontal/vertical lines
def ChoosePath(ttl, step):
	if step < 2:
		choice = random.randint(1, 2)
		return choice
	else:
		rand_path = random.random()
		if step == 2:
			if rand_path <= .146:
				choice = 3
			else:
				choice = random.randint(1, 2)
		elif step == 3:
			if rand_path <= .192:
				choice = 3
			else:
				choice = random.randint(1, 2)
		elif step == 4:
			if rand_path <= .238:
				choice = 3
			else:
				choice = random.randint(1, 2)
		elif step == 5:
			if rand_path <= .284:
				choice = 3
			else:
				choice = random.randint(1, 2)
		elif step >= 6:
			if rand_path <= .33:
				choice = 3
			else:
				choice = random.randint(1, 2)
	return choice

# Function randomly chooses color to fill boxes
def ColorPath(ttl, step, choice, x_1, y_1, x_2, y_2):
	color = random.randint(1, 5)
	if color == 1: 
		color = 'white'
	elif color == 2:
		color = 'blue'
	elif color == 3:
		color = 'red'
	elif color == 4:
		color = 'yellow' 
	elif color == 5:
		color = 'white'

	Square(ttl, color, x_1, y_1, x_2, y_2)

# Function randomly configures the painting		
def drawPicture(ttl, step, x_1, x_2, y_1, y_2):
	if step == 0:
		return
	else:
		choice = ChoosePath(ttl, step)

		# Decides if vertical line should be present randomly
		if choice == 1:
			if not ((x_2 - (50 // step)) - (x_1 + 50 // step)) < 0:
				x = random.randint(x_1 + 50 // step, x_2 - 50 // step)
			else:
				x = (x_1 + x_2) // 2
			Line(ttl, x, y_1, x, y_2)

			if step == 1:
				ColorPath(ttl, step, choice, x, y_1, x_2, y_2)

			drawPicture(ttl, step - 1, x, x_2, y_1, y_2)
			drawPicture(ttl, step - 1, x_1, x, y_1, y_2)

		# Decides if horizontal lie should be present randomly
		elif choice == 2:
			if not ((y_2 - 50 // step) - (y_1 + 50 // step)) < 0:
				y = random.randint(y_1 + 50 // step, y_2 - 50 // step)
			else:
				y = (y_1 + y_2) // 2
			Line(ttl, x_1, y, x_2, y)

			if step == 1:
				ColorPath(ttl, step, choice, x_1, y, x_2, y_2)

			drawPicture(ttl, step - 1, x_1, x_2, y, y_2) 
			drawPicture(ttl, step - 1, x_1, x_2, y_1, y)
		elif choice == 3:
			drawPicture(ttl, step - 1, x_1, x_2, y_1, y_2)
		

def main():

  # Creates turtle object
  ttl = turtle.Turtle()
  
  # Creates title and screen size
  turtle.title ('Mondrian.py')
  turtle.setup (800, 800, 0, 0)

  print("Mondrian Composition")
  print()
  step = int(input('Enter a step of recursion between 1 and 6: '))

  ttl.speed(0)
  ttl.pensize(6)
  ttl.color('black')
  turtle.hideturtle()

  # Draws Mondrian design
  drawPicture(ttl, step, -400, 400, -400, 400)
  ttl.penup()
  ttl.goto(-400, -400)
  ttl.pendown()
  ttl.goto(-400, 400)
  ttl.goto(400, 400)
  ttl.goto(400, -400)
  ttl.goto(-400, -400)
  ttl.penup()

  # Saves .eps file
  picture = turtle.getscreen().getcanvas()
  picture.postscript(file = './Bella_Shah_Mondrian.eps')

  # Persists drawing 
  turtle.bye()
  
main()