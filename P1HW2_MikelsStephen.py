#Budget Workpage
#02/08/2023
#CTI-110 P1HW2 - Travel Expense
#Stephen Mikels
## ******************** Pseudocode **********************
#display "this program calculates and displays travel expenses"
#ask user to input budget
#ask user to input travel destination
#ask user to input gas
#ask user to input hotel
#ask user to input food
#set total expense
#set remaining balance
#display "------------Travel Expenses-------------"
#display location
#display budget
#display fuel cost
#display gas cost
#display hotel cost
#display remaining balance
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
print('Initial Budget: ',budget,'\n')
print('\nFuel: ',gas)
print('Accomodation: ',hotel)
print('Food: ',food,'\n')
print('\nRemaining Balance: ',left)
