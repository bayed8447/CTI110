# This program draws two connected diamonds using Python
# Turtle Graphics.
#
# Position starts on left diamond's 9 oclock point.  Pen
# goes down.  Pen moves to right diamond's 12 oclock point.
# Pen moves to right diamond's 3 oclock point.  Pen moves
# to right diamond's 6 oclock point.  Pen moves to left
# diamond's 12 oclock point.  Pen moves to left diamond's
# 9 oclock point.  This is the starting and end position.
# The connected diamonds drawing should be complete.  Pen
# goes up.  Program is complete.
#
# March 3rd, 2020
# CTI-110 P2HW2 - Turtle Graphics
# Dale Baye
#

# Import turtle graphic object
import turtle


# Set the window size
turtle.setup(600, 600)

# Setup the turtle
turtle.penup()
turtle.hideturtle()

# Create named constants for the diamond coordinates
L_DIAMOND_12_X = -100
L_DIAMOND_12_Y = 100

L_DIAMOND_9_X = -200
L_DIAMOND_9_Y = 0

L_DIAMOND_6_X = -100
L_DIAMOND_6_Y = -100

R_DIAMOND_12_X = 100
R_DIAMOND_12_Y = 100

R_DIAMOND_3_X = 200
R_DIAMOND_3_Y = 0

R_DIAMOND_6_X = 100
R_DIAMOND_6_Y = -100

# Draw the connected diamonds
turtle.goto(L_DIAMOND_9_X, L_DIAMOND_9_Y)
turtle.pendown()
turtle.goto(L_DIAMOND_6_X, L_DIAMOND_6_Y)
turtle.goto(R_DIAMOND_12_X, R_DIAMOND_12_Y)
turtle.goto(R_DIAMOND_3_X, R_DIAMOND_3_Y)
turtle.goto(R_DIAMOND_6_X, R_DIAMOND_6_Y)
turtle.goto(L_DIAMOND_12_X, L_DIAMOND_12_Y)
turtle.goto(L_DIAMOND_9_X, L_DIAMOND_9_Y)
turtle.penup()

turtle.done()
