
# File: ColorShapes.py

# Description: Draws filled in shapes

import turtle

def main():
  # put label on top of page
  turtle.title ('Colorful Shapes')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # draw a triangle
  turtle.pensize(1)
  turtle.penup()
  turtle.goto (-20, -50)
  turtle.pendown()
  #turtle.begin_fill()
  #turtle.color ('red')
  #turtle.circle (50, steps = 3)
  #turtle.end_fill()

  

  # write header
  turtle.penup()
  turtle.goto (-100, 50)
  turtle.write ('Cool Colorful Shapes', font = ('Times', 18, 'bold'))

  # hide turtle
  turtle.hideturtle()

  # persist drawing
  turtle.done()

main()