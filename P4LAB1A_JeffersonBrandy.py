#Brandy Jefferson
#22 April 2026
#P4LAB1A
#Use turtle to draw a square and a triangle

#Import the turtle library
import turtle

#Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#Set turtle options
pen.pensize(5)
pen.pencolor("blue")
pen.shape("arrow")

#Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

#Code to draw the shapes
for side in range(4):
    pen.forward(100)
    pen.left(90)

#While loop that executes 3 times
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    print (sides)
    sides = sides - 1

#Wait for user to close windown
win.mainloop()
