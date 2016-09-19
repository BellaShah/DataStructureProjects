import turtle 

def main():
	#put label on top of page
	turtle.title("Hello World")

	#set up screen size
	turtle.setup(500, 500, 0, 0)

	#move turtle to origin
	turtle.penup()
	turtle.goto(0,0)

	# set the color to navy turtle
	turtle.color("navy")

	# write the message
	turtle.write("Hello World", font = ("Times New Roman", 36, "bold"))

	# persist the drawing 
	turtle.done()


main()