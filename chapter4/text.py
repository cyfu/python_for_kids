'''
Using Python’s Turtle Module
'''
import turtle

'''
Creating a Canvas
'''
t = turtle.Pen()

'''
Moving the Turtle
'''
t.forward(50)
t.left(90)
t.forward(50)

t.left(90)
t.forward(50)

t.left(90)
t.forward(50)

t.left(90)

#erase the canvas
#clears the canvas and puts the turtle back at its starting position.
t.reset()

#clears the screen and leaves the turtle where it is.
t.clear()

# More samples
t.reset()
t.backward(100)
# lift the pen off the canvas
t.up()
t.right(90)
t.forward(20)
t.left(90)
# put the pen down on the canvas
t.down()
t.forward(100)

