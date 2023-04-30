# CTI-110
# P3HW2 - Salary
# Stephen Mikels
# 20/03/2023
#Asks the user to enter name of employee
#Ask user to enter number of hours the employee worked this week
#Ask user to enter employee's pay rate
#Evaluate if employee has worked overtime (more than 40 hours).
#If yes, calculate the amount owed to employee for overtime hours
#Calculate amount employee should be paid for regular hours worked.
#Display gross pay (total amount that should be paid to employee)
#The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).
name=input('User Name:')
hours=float(input('Hours:'))
wage=float(input('Wage:'))
ot=hours-40
otwage=wage+(wage/2)
if ot<=0:
    ot=0
    otpay=0
else:
    otpay=ot*otwage
pay=hours*wage
gross=pay+otpay
print('\n--------------------------------------------------------------------------------------------\n')
print('Employee:',name)
print('\nHours Worked     Wage        OverTime        OverTime Pay        RegHr Pay       Gross Pay')
print('=============================================================')
print(f'    {hours:.2f}              ${wage:.2f}         {ot:.2f}                 ${otpay:.2f}                  ${pay:.2f}            ${gross:.2f}')
