#Budget Workpage
#02/22/2023
#CTI-110 P2HW2 - List
#Stephen Mikels
## ******************** Pseudocode **********************
#display "this program will tell you the lowest, highest, sum, and average of your tests."
#ask user to input 6 module test grades to 2nd decimal
#display list of grades entered
#display lowest grade entered
#display highest grade entered
#display sum of grades
#display the average of the grades
print('This program will tell you the lowest, highest, sum, and average of your tests.')
mod0=float(input('Enter grade from Module 1: '))
mod1=float(input('Enter grade from Module 2: '))
mod2=float(input('Enter grade from Module 3: '))
mod3=float(input('Enter grade from Module 4: '))
mod4=float(input('Enter grade from Module 5: '))
mod5=float(input('Enter grade from Module 6: '))
list=[mod0,mod1,mod2,mod3,mod4,mod5]
print('\n You entered', list)
print('\n----------Results----------')
avg=sum(list)/len(list)
print('\nLowest Grade:',min(list))
print('Highest Grade:',max(list))
print('Sum of Grades:',sum(list))
print(f'Average Grade: {avg:.2f}')
