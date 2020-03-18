#################################################################################
# This program requests two primary colors via user input and mixes the colors  #
# to provide user with their secondary color results.                           #
#                                                                               #
# Pseudocode:                                                                   #
# Create the variable, "color1" while requesting typed input from user.         #
# Create the variable, "color2" while requesting typed input from user.         #
# Display a response with secondary color results.                              #
# If the user provides invalid input, display error message and explanation.    #
#                                                                               #
#                                                                               #
# CTI-110                                                                       #
# P3HW1 - Color Mixer                                                           #
# Dale Baye                                                                     #
# 03/17/2020                                                                    #
#################################################################################


# Display Program Title.  Or possibly crash computer!
print('')
print('*********************')
print('***  COLOR MIXER  ***')
print('*********************')
print('')

# Provide program instructions to user.
print('This program will teach you how to mix primary colors and create secondary colors.')
print('Your primary colors are red, yellow and blue.')
print('Please type them one at a time and in lower case.')
print('Be sure not to use the same option for your first and second color.')
print('')
print('')

# This section displays color options to user. Create the color1 and color2 variables.
#
# Primary Color Options
color1 = input('Enter your first primary color: ')
color2 = input('Enter your second primary color: ')

# This section analyzes user input/variables "color1" and "color2" and provides
# the secondary color result of their primary color choices.
#
# Secondary Color Results
if color1 == "red" and color2 == "blue":
    print('Congratulations! You made purple!')
elif color1 == "blue" and color2 == "red":
    print('Congratulations! You made purple!')

elif color1 == "yellow" and color2 == "blue":
    print('Congratulations! You made green!')
elif color1 == "blue" and color2 == "yellow":
    print('Congratulations! You made green!')

elif color1 == "red" and color2 == "yellow":
    print('Congratulations! You made orange!')
elif color1 == "yellow" and color2 == "red":
    print('Congratulations! You made orange!')
else:          
# This section displays error messages and explanations if user did not type valid options
    print('')
    print('')
    # Give error messages explaining likely mistakes.
    print('OOPS!!! You must not have typed red, yellow or blue.')
    print('Check your spelling and be sure to type in lower case.') 
    print('Also, you must choose two different colors.')
          




