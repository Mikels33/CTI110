#CTI-110 P3HW1 Debugging
#20/03/2023
#Stephen Mikels
#This program takes a number grade , determines average and displays letter grade for average.
#Enter grades for six modules
#add grades entered to a list
#show lowest
#show highest
#show sum of grades
#show average
#determine letter grade for average
mod1=float(input('Enter grade for Module 1: '))
mod2=float(input('Enter grade for Module 2: '))
mod3=float(input('Enter grade for Module 3: '))
mod4=float(input('Enter grade for Module 4: '))
mod5=float(input('Enter grade for Module 5: '))
mod6=float(input('Enter grade for Module 6: '))
grades = [mod1,mod2,mod3,mod4,mod5,mod6]
print('\n============Results==============\n')
low=min(grades)
high=max(grades)
total=sum(grades)
avg=total/len(grades)
print('\nLowest Grade:',min(grades))
print('Highest Grade:',max(grades))
print('Sum of Grades:',sum(grades))
print(f'Average Grade: {avg:.2f}')
print('\n==================================\n')
if avg>=90:
    print('Your average grade is: A')
elif 90>=avg>=80:
    print('Your average grade is: B')
elif 80>=avg>=70:
    print('Your average grade is: C')
elif 70>=avg>=60:
    print('Your average grade is: D')
else:
    print('Your average grade is: F')





