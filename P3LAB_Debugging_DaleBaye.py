#################################################################################
#                                                                               #
# CTI-110                                                                       #
# P3LAB - Debugging                                                             #
# Dale Baye                                                                     #
# 03/24/2020                                                                    #
#                                                                               #
# Description:                                                                  #
# This program determines the letter grade by performing calculations on a      #
# number score provided via user input and displays the letter grade.           #
#                                                                               #
# Pseudocode:                                                                   #
# Input the number score of grade                                               #
# If score >= 90                                                                #
#       Display "Your grade is an A."                                           #
# Else If score >= 80 and <90                                                   #
#       Display "Your grade is a B."                                            #
# Else If score >= 70 and <80                                                   #
#       Display "Your grade is a C."                                            #
# Else If score >= 60 and <70                                                   #
#       Display "Your grade is a D."                                            #
# Else                                                                          #
#       Display "Your grade is an F."                                           #
#                                                                               #
#################################################################################

# Display Program Title.
print('')
print('************************************************************************')
print('* ******************************************************************** *')
print('* *                                                                  * *')
print('* *                        GRADE CALCULATOR                          * *')
print('* *                                                                  * *')
print('* ******************************************************************** *')
print('************************************************************************')
print('')

# Provide program details and instructions to user.
print('This program calculates the letter grade based on your number grade')
print('Enter your score when prompted. ')
print('Please use numerical values only.')
print('')

# Calculate the letter grade based on user's input.
score = int(input('Please enter your number score: '))
if score >= 90:
    print('Your grade is an A. ')
elif score  >= 80 and score < 90:
    print('Your grade is a B. ')
elif score  >= 70 and score < 80:
    print('Your grade is a C. ')
elif score  >= 60 and score < 70:
    print('Your grade is a D. ')
else:
    print('Your grade is an F. ')




