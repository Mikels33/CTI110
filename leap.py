year=int(input('Enter Year:'))
ncen=year%4
div=year%100
if div==0:
    cenyr=year%400
    if cenyr==0:
        print(year,'- leap year.')
    else:
        print(year,'- not a leap year.')
elif ncen==0:
    print(year,'- leap year.')
    print(year,'- not a leap year.')
