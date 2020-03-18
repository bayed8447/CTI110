#################################################################################
#                                                                               #
# CTI-110                                                                       #
# P3T1 - Areas of Rectangles                                                    #
# Dale Baye                                                                     #
# 03/17/2020                                                                    #
#                                                                               #
# Description:                                                                  #
# This program calculates the area of rectangles based on the length and width  #
# provided by user inputs and displays which is greater.                        #
#                                                                               #
# Pseudocode:                                                                   #
# Input the length and width of rectangle 1.                                    #
# Input the length and width of rectangle 2.                                    #
# Calculate the area of rectangle 1.                                            #
# Calculate the area of rectangle 2.                                            #
# If area1 > area2                                                              #
#       Display "Rectangle 1 has the greatest area."                            #
# else if area2 > area1                                                         #
#       Display "Rectangel 2 has the greatest area."                            #
# else                                                                          #
#       Display "Both rectangles have the same area."                           #
#                                                                               #
#################################################################################

# Display Program Title.
print('')
print('************************************************************************')
print('* ******************************************************************** *')
print('* *                                                                  * *')
print('* *                        AREAS of RECTANGLES                       * *')
print('* *                                                                  * *')
print('* ******************************************************************** *')
print('************************************************************************')
print('')

# Provide program details and instructions to user.
print('This program calculates the area of two rectangles and display which is')
print('greater.  Enter the length and width of each rectangle when prompted. ')
print('Please use numerical values only.')
print('')

# Get the dimensions of rectangle 1.
r1length = int(input('Please enter the length of rectangle 1: '))
r1width = int(input('Please enter the width of rectangle 1: '))
print('')

# Get the dimensions of rectangle 2.
r2length = int(input('Please enter the length of rectangle 2: '))
r2width = int(input('Please enter the width of rectangle 2: '))
print('')

# Calculate the areas of the two rectangles.
area1 = r1length * r1width
area2 = r2length * r2width

# Determine which rectangle has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both rectangles have the same area.')
