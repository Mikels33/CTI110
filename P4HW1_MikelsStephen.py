#Budget Workpage
#04/19/2023
#CTI-110 P4HW1 - Score List
#Stephen Mikels
## ******************** Pseudocode **********************
#display "this program will tell you the lowest, highest, sum, and average of your tests."
#ask user to input number of scores
#ask user to input scores from 0-100
#display list of grades entered
#display lowest grade entered
#display highest grade entered
#display the average of the grades
print('This program will tell you the lowest grade, a modded list dropping the lowest, the average of your modified scores, and the modified letter grade')
score_list=[]
cscore=1
num_scores=int(input('How many scores do you want to enter? '))
while cscore<=num_scores:
    score=float(input(f'\nEnter score #{cscore} :'))
    if score<0 or score>100:
        print('\nINVALID SCORE ENTERED!!!!\nEntered score must be between 0 and 100.')
    else:
        score_list.append(score)
        cscore+=1
print('\n----------Results----------')
print('\nLowest Grade:',min(score_list))
score_list.remove(min(score_list))
mod_list=score_list
avg=sum(mod_list)/len(mod_list)
print('Modified List:',mod_list)
print(f'Average Grade: {avg:.2f}')
if avg<60:
    lettergrade='F'
if 59<avg<70:
    lettergrade='D'
if 69<avg<80:
    lettergrade='C'
if 79<avg<90:
    lettergrade='B'
if 89<avg<=100:
    lettergrade='A'
print('Grade:',lettergrade)
