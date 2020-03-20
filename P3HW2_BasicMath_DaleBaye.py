#################################################################################
#                                                                               #
# CTI-110                                                                       #
# P3HW2 - Basic Math                                                            #
# Dale Baye                                                                     #
# 03/19/2020                                                                    #
#                                                                               #
# Description:                                                                  #
# This program performs simple calculations on a pair of numbers provided via   #
# user input.                                                                   #
#                                                                               #
# Pseudocode:                                                                   #
# Display Program Title                                                         #
# Display Explanation of program and instructions.                              #
# Request number 1 and save as variable num1.                                   #
# Request number 2 and save as variable num2.                                   #
# Display Program Menu Options                                                  #
# Request number of menu option to perform.                                     #
# Calculate the sum of num1, num2 and save as variable value1                   #
# Calculate the product of num1, num2 and save as variable value2               #
# Calculate the difference of num1, num2 and save as variable value3            #
# Request menu option number from user and save as variable option1             #
# If option1 = 1, Display value1                                                #
# Else If option1 = 2, Display value2                                           #
# Else If option1 = 3, Display value3                                           #
# Else If option1 = 4, Display EXITING PROGRAM!                                 #
# Else display INVALID OPTION!                                                  #
#                                                                               #
#################################################################################

# Display Program Title.
print('')
print('************************************************************************')
print('* ******************************************************************** *')
print('* *                                                                  * *')
print('* *                        BASIC MATH CALCULATOR                     * *')
print('* *                                                                  * *')
print('* ******************************************************************** *')
print('************************************************************************')
print('')

# Provide program details and instructions to user.
print('This program performs simple calculations with a set of numbers you')
print('provide.  Enter two numbers when prompted.  Enter the number of the menu')
print('option you wish to perform with your numbers or to exit the program.')
print('')

# Get two numbers from user.
num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))
print('')
print('')

# Display menu options to user.
print('--------MENU---------')
print(' 1) Add Numbers')
print(' 2) Multiply Numbers')
print(' 3) Subtract Numbers')
print(' 4) Exit')
print('---------------------')
print('')

# Perform math and convert answers to variables
value1 = num1 + num2
value2 = num1 * num2
value3 = num1 - num2

# Get menu option from user and provide value of value1, value2 or value3.
# Or terminate program if they chose option 4
option1 = int(input('Enter NUMBER for Menu Option you wish to perform: '))
if option1 == 1:
    print (num1, ' + ', num2, ' = ', value1)
elif option1 == 2:
    print (num1, ' x ', num2, ' = ', value2)
elif option1 == 3:
    print (num1, ' - ', num2, ' = ', value3)
elif option1 == 4:
    print ('')
    print (' EXITING PROGRAM...')
else:
    print(' INVALID OPTION!!! ')
    print(' Please enter a number 1 - 4')
                    

