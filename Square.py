import turtle

# draw a square of a given side
# starting a upper left corner (x,y)

def drawSquare(ttl,x,y,side):
	ttl.penup()
	ttl.goto(x,y)
	ttl.setheading(0) # set the pen in the +ve x direction
	ttl.pendown()
	for iter in range (4):
		ttl.forward(side)
		ttl.right(90)
	ttl.penup()





def main():
	# put label on top of page
	turtle.title("Squares")

	# setup screen size
	turtle.setup(800,800,0,0)

	# create turtle object
	ttl = turtle.Turtle()

	# decide on the shape
	ttl.shape ("turtle")

	# decide on speed
	ttl.speed(10)

	# assign a color 
	ttl.color("red")

	# draw multiple square
	drawSquare(ttl,-50,-50,50)
	drawSquare(ttl,0,0,50)
	drawSquare(ttl,50,50,50)
	drawSquare(ttl,-50,50,150)

	# fill a closed region
	ttl.fillcolor('purple')
	ttl.begin_fill()
	drawSquare(ttl,0,0,50)
	ttl.end_fill()

	# persist drawing
	turtle.done()


main()