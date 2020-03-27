#################################################################################
#                                                                               #
# CTI-110                                                                       #
# P4T1A - Turtle Graphic                                                        #
# Dale Baye                                                                     #
# 03/26/2020                                                                    #
#                                                                               #
# Description:                                                                  #
# This program draws 100 squares to create an interesting pattern               #
#                                                                               #
# Pseudocode:                                                                   #
# Import Turtle Graphic                                                         #
# Turn left 90 degrees for correct orientation                                  #
# Set Length to 505                                                             #
# Set Count to 0                                                                #
# While count < 100                                                             #
#       Move turtle forward (Length)                                            #
#       Turn Left 90 degrees                                                    #
#       Move turtle forward (Length)                                            #
#       Turn Left 90 degrees                                                    #
#       Move turtle forward (Length)                                            #
#       Turn Left 90 degrees                                                    #
#       Move turtle forward (Length)                                            #
#       Turn Left 90 degrees                                                    #
#       Increase Count by 1                                                     #
#       Subtract 5 from (Length)                                                #
# Repeat until count reaches 100                                                #
#                                                                               #
#################################################################################

# Display Program Title.
print('')
print('************************************************************************')
print('* ******************************************************************** *')
print('* *                                                                  * *')
print('* *                  TURTLE GRAPHIC - SQUARE PATTERN                 * *')
print('* *                                                                  * *')
print('* ******************************************************************** *')
print('************************************************************************')
print('')

# Provide program details to user.
print('This program draws 100 squares to create an interesting pattern')
print('')


# Import turtle graphic object
import turtle

# Setup the turtle
turtle.hideturtle()
turtle.left(90)
turtle.speed(0)

# Named constants
NumLength = 505

# Draw 100 squares
count = 0
while count < 100:
          turtle.forward(NumLength)
          turtle.left(90)
          turtle.forward(NumLength)
          turtle.left(90)
          turtle.forward(NumLength)
          turtle.left(90)
          turtle.forward(NumLength)
          turtle.left(90)
          count = count + 1
          NumLength = NumLength - 5

turtle.penup()
turtle.done()

