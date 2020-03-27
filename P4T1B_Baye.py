#################################################################################
#                                                                               #
# CTI-110                                                                       #
# P4T1B - Turtle Graphic                                                        #
# Dale Baye                                                                     #
# 03/26/2020                                                                    #
#                                                                               #
# Description:                                                                  #
# This program draws my initials                                                #
#                                                                               #
# Pseudocode:                                                                   #
# Import Turtle Graphic                                                         #
# Turn Left 90 degrees for correct orientation                                  #
# Move Forward 235 spaces                                                       #
# Turn Right 90 degrees                                                         #
# Move Forward 50 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 60 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 60 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 75 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 60 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 60 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 50 spaces                                                        #
# Pull pen up                                                                   #
# Move backwards 200 spaces                                                     #
# Put pen down                                                                  #
# Turn Right 90 degrees                                                         #
# Move Forward 235 spaces                                                       #
# Turn Right 90 degrees                                                         #
# Move Forward 50 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 30 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 30 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 37 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 30 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 30 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 50 spaces                                                        #
# Turn Right 180 degrees                                                        #
# Move Forward 50 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 30 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 30 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 37 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 30 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 30 spaces                                                        #
# Turn Right 30 degrees                                                         #
# Move Forward 50 spaces                                                        #
# Pull Pen Up                                                                   #
#                                                                               #
#################################################################################

# Display Program Title.
print('')
print('************************************************************************')
print('* ******************************************************************** *')
print('* *                                                                  * *')
print('* *                     TURTLE GRAPHIC - INITIALS                    * *')
print('* *                                                                  * *')
print('* ******************************************************************** *')
print('************************************************************************')
print('')

# Provide program details to user.
print('This program draws my initials')
print('')


# Import turtle graphic object
import turtle

# Setup the turtle
win = turtle.Screen()
win.bgcolor("black")
win.title("Hello World!")
alexa = turtle.Turtle()
alexa.color("orange")
alexa.pensize(4)
alexa.speed(0)

# Rotate left 90 degrees for correct orientation
alexa.left(90)

# Draw letter D
alexa.forward(235)
alexa.right(90)
alexa.forward(50)
alexa.right(30)
alexa.forward(60)
alexa.right(30)
alexa.forward(60)
alexa.right(30)
alexa.forward(75)
alexa.right(30)
alexa.forward(60)
alexa.right(30)
alexa.forward(60)
alexa.right(30)
alexa.forward(50)

# Move over for next letter
alexa.penup()
alexa.backward(200)
alexa.pendown()

# Draw letter B
alexa.right(90)
alexa.forward(235)
alexa.right(90)
alexa.forward(50)
alexa.right(30)
alexa.forward(30)
alexa.right(30)
alexa.forward(30)
alexa.right(30)
alexa.forward(37)
alexa.right(30)
alexa.forward(30)
alexa.right(30)
alexa.forward(30)
alexa.right(30)
alexa.forward(50)
alexa.right(180)
alexa.forward(50)
alexa.right(30)
alexa.forward(30)
alexa.right(30)
alexa.forward(30)
alexa.right(30)
alexa.forward(37)
alexa.right(30)
alexa.forward(30)
alexa.right(30)
alexa.forward(30)
alexa.right(30)
alexa.forward(50)
alexa.penup()

alexa.done()

Win.mainloop()
