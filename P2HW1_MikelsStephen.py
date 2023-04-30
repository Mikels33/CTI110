#Budget Workpage
#02/20/2023
#CTI-110 P2HW1 - Travel Expense Expanded
#Stephen Mikels
## ******************** Pseudocode **********************
#display "this program calculates and displays travel expenses"
#ask user to input budget in dollars
#ask user to input travel destination
#ask user to input gas in dollars
#ask user to input hotel in dollars
#ask user to input food in dollars
#set total expense in dollars
#set remaining balance in dollars
#display "------------Travel Expenses-------------"
#display location
#display budget in dollars
#display fuel cost in dollars
#display gas cost in dollars
#display hotel cost in dollars
#display remaining balance in dollars
print('\nThis program calculates and displays travel expenses')
budget = float(input('\nEnter Budget: '))
destination = input('Travel Destination: ')
gas = float(input('\nRough gas cost: '))
hotel = float(input('Rough accomodation/hotel cost: '))
food = float(input('Rough food cost: '))
expense = gas + hotel + food
left = budget - expense
print('\n------------Travel Expenses-------------')
print('\nLocation: ',destination)
print(f'Initial Budget: ${budget:.2f}\n')
print(f'\nFuel: ${gas:.2f}')
print(f'Accomodation: ${hotel:.2f}')
print(f'Food: ${food:.2f}\n')
print(f'\nRemaining Balance: ${left:.2f}')
