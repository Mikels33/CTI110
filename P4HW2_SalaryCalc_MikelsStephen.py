# CTI-110
# P4HW2 - Salary Calculator
# Stephen Mikels
# 03/04/2023
#Asks the user to enter name of employee
#Ask user to enter number of hours the employee worked this week
#Ask user to enter employee's pay rate
#Evaluate if employee has worked overtime (more than 40 hours).
#If yes, calculate the amount owed to employee for overtime hours
#Calculate amount employee should be paid for regular hours worked.
#Display gross pay (total amount that should be paid to employee)
#The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).
#Repeat using a name
#Terminate when "Done" is input
#Display total employees
#Display total ot pay
#Display total reg pay
#Display total Gross Pay
emp=0
tototpay=0
totregpay=0
name=input('Enter employee name or "done" to terminate:')
terminate="done"
while name!=terminate:
    emp+=1
    hours=float(input('Hours:'))
    wage=float(input('Wage:'))
    ot=hours-40
    otwage=wage+(wage/2)
    if ot<=0:
        ot=0
        otpay=0
        pay=hours*wage
    else:
        ghours=40
        otpay=ot*otwage
        pay=ghours*wage
    gross=pay+otpay
    print('Employee:',name)
    print('\nHours Worked     Wage        OverTime        OverTime Pay        RegHr Pay       Gross Pay')
    print('============================================================================================')
    print(f'{hours:.2f}{wage:16.2f}{ot:13.2f}{otpay:18.2f}{pay:20.2f}{gross:17.2f}')
    tototpay+=otpay
    totregpay+=pay
    totgross=tototpay+totregpay
    name=input('\nEnter employee name or "done" to terminate:')
print('\n--------------------------------------------------------------------------------------------\n')
print(f'Total Employees Entered: {emp}')
print(f'Total Overtime Paid: ${tototpay:.2f}')
print(f'Total Regular Hours Paid: ${totregpay:.2f}')
print(f'Total Gross Pay: ${totgross:.2f}')
