# This program predicts annual profits based on user input.
# This is performed by calculating 23% of projected total sales.
# 02/18/2020
# CTI-110 P2T1 - Sales Prediction
# Dale Baye
#

# Get the projected total sales.
total_sales = float( input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))


