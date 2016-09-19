#  File: Train.py

#  Description: This program creates a train out of turtle graphics

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: February 27, 2016

#  Date Last Modified:February 27, 2016
import turtle, math

# Gives position
def Position (ttl,x,y):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()

# Draws Railing
def Rails(ttl, length, width, x, y):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.goto(x, y - width)
	ttl.goto(x + length, y - width)
	ttl.goto(x + length, y)
	ttl.penup()
	return(Studs(ttl, x, y))

# Draws studs on railtrack
def Studs(ttl, x, y):
	if (x > 250):
		return ()
	else:
		return(Rails(ttl, 20, 5, x + 40, y))

# Draws Vertical Bolts on train
def VertBolts(ttl, x, y, size):
	if (x > 310):
		return ()
	else:
		return(VertCircleBolts(ttl, x, y, size))

# Draws Vertical Bolts on train
def VertCircleBolts(ttl, x, y, size):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.begin_fill()
	ttl.circle(size)
	ttl.end_fill()
	ttl.penup()
	return (VertBolts(ttl, x + 10, y, size))


# Draws horizontal Bolts on train
def HorizBoltz(ttl, x, y, size):
	if (y > 102):
		return ()
	else:
		return(HorizCircleBoltz(ttl, x, y, size))

# Draws horizontal Bolts on train
def HorizCircleBoltz(ttl, x, y, size):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.begin_fill()
	ttl.circle(size)
	ttl.end_fill()
	ttl.penup()
	return (HorizBoltz(ttl, x, y + 10, size))

# Draws a straight line
def drawLine(ttl, x, y, x2, y2):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.goto(x2, y2)
	ttl.penup()

# Draws a circle
def Circle(ttl, x, y, dimension):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.circle(dimension)
	ttl.penup()

# Draws a polygon
def Shape(ttl, x, y, dimension, step):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.circle(dimension, steps = step)
	ttl.penup()

# Draws arc for wheel 
def arc (ttl, x, y, size, degrees):
	ttl.goto(x, y)
	ttl.pendown()
	for i in range (degrees):
		ttl.forward(size)
		ttl.right(1)
	ttl.penup()

# Draws rectangle
def Rectangle(ttl, x, y, length, width):
	drawLine(ttl, x, y, x + length, y)
	drawLine(ttl, x + length, y, x + length, y + width)
	drawLine(ttl, x + length, y + width, x, y + width)
	drawLine(ttl, x, y + width, x, y)

# Draws spokes
def Spokes(ttl, x, y, Size):
	degrees = 360
	ttl.goto(x, y)
	ttl.pendown()
	if Size == .25:
		for i in range (degrees):
			if (i % 45 == 0):
				ttl.left(100)
				ttl.forward(30)
				ttl.backward(30)
				ttl.right(100)
				ttl.left(80)
				ttl.forward(30)
				ttl.backward(30)
				ttl.right(80)
			ttl.forward(Size)
			ttl.right(1)
	elif Size == .15:
		for i in range (degrees):
			if (i % 45 == 0):
				ttl.left(100)
				ttl.forward(26.5)
				ttl.backward(26.5)
				ttl.right(100)
				ttl.left(80)
				ttl.forward(26.5)
				ttl.backward(26.5)
				ttl.right(80)
			ttl.forward(Size)
			ttl.right(1)
	ttl.penup()

#will draw the inner and outer part of the wheel with the spoke function
def Wheels(ttl, x, y, radius, Size):
	Circle(ttl, x, y, radius)
	Circle(ttl, x, y + 10, radius - 10)
	if radius == 55:
		Spokes(ttl, x, y + (radius + 15), Size)
	elif radius == 45:
		Spokes(ttl, x, y + (radius + 7.5), Size)


def main():
  # Sets title of drawing
  turtle.title ('Train.py')

  # Sets up screen size
  turtle.setup (800, 800, 0, 0)

  # Creates turtle object
  ttl1 = turtle.Turtle()
  ttl1.pensize(3)

  # Draws Rail
  ttl1.color('#AF002A')
  drawLine(ttl1, -350, -200, 350, -200)
  drawLine(ttl1, -350, -220, 350, -220)
  Studs(ttl1, -350, -220)

  # Creates another turtle object
  ttl2 = turtle.Turtle()
  ttl2.pensize(3)

  # Draws Wheels
  ttl2.color('#8A2BE2')
  Wheels(ttl2, -200, -200, 55, .25)
  Wheels(ttl2, 20.74, -200, 45, .15)
  Wheels(ttl2, 214.26, -200, 45, .15)
  ttl2.color('blue')

  # Draws back of train
  drawLine(ttl2, -300, 150, -300, -150)
  drawLine(ttl2, -300, -150, -272.5, -150)
  ttl2.left(90)
  arc(ttl2, -272.5, -150, 1.25, 180)
  ttl2.left(90)
  ttl2.pendown()
  ttl2.forward(27.5)
  ttl2.left(90)
  ttl2.forward(300)
  ttl2.left(90)
  ttl2.forward(197)
  Rectangle(ttl2, -330, 151, 260, 40)

  # Draws top of train
  drawLine(ttl2, -101.76, 110, 312.20, 110)
  Rectangle(ttl2, 30, 110, 70, 25)
  Rectangle(ttl2, 50, 135, 30, 12)

  # Draws smokething
  ttl2.color("#2A52BE")
  drawLine(ttl2, 190, 110, 160, 196.6)
  ttl2.goto(160, 196.6)
  ttl2.pendown()
  ttl2.right(180)
  ttl2.forward(100)
  ttl2.left(120)
  ttl2.forward(30)
  ttl2.left(60)
  ttl2.forward(70)
  ttl2.left(60)
  ttl2.forward(30)
  ttl2.penup()
  ttl2.right(60)
  drawLine(ttl2, 230, 110, 260, 196.6)

  # Draws bottom of train
  ttl2.goto(-101.76, -149)
  ttl2.penup()
  ttl2.right(180)
  ttl2.pendown()
  ttl2.forward(50)
  ttl2.left(90)
  arc(ttl2, -51.76, -148.75, 1.25, 180)
  ttl2.pendown()
  ttl2.left(90)
  ttl2.forward(50)
  ttl2.left(90)
  arc(ttl2, 141.76, -148.46, 1.25, 180)
  ttl2.left(90)
  ttl2.pendown()
  ttl2.forward(27.5)
  ttl2.penup()
  drawLine(ttl2, 312.20, -147.21, 312.20, 110)

  # Draws track
  Rectangle(ttl2, -102, -5, 414, 15)
  ttl2.color("#E52B50")
  VertBolts(ttl2, -96, 0, 2)
  Rectangle(ttl2, -10, 10, 15, 100)
  HorizBoltz(ttl2, -3, 16, 2)
  Rectangle(ttl2, 207, 10, 15, 100)
  HorizBoltz(ttl2, 214, 16, 2)

  #Draws front of train
  ttl2.penup()
  ttl2.goto(312.50, -147.21)
  ttl2.pendown()
  ttl2.forward(60)
  ttl2.left(120)
  ttl2.forward(60)
  ttl2.left(60)
  ttl2.forward(30)
  Rectangle(ttl2, 312.20, -70, 20, 150)
  Rectangle(ttl2, 332.20, -35, 10, 75)

  # Draws Windows
  ttl2.color('#C9FFE5')
  ttl2.begin_fill()
  Rectangle(ttl2, -280, 40, 70, 80)
  ttl2.end_fill()
  ttl2.begin_fill()
  Rectangle(ttl2, -190, 40, 70, 80)
  ttl2.end_fill()

  ttl2.color('#E52B50')
  Rectangle(ttl2, -281, 41, 71, 81)
  Rectangle(ttl2, -191, 41, 71, 81)

  # Hides turtle 
  ttl2.hideturtle()

  # Finishes drawing
  turtle.done()

main()