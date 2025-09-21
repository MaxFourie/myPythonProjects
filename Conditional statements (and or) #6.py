number = float(input('input your number please: '))
if number >= 5 and number <= 10:
        print('your number is between 5 and 10')
else: print('your number is not between 5 and 10')

myNum = float(input('pick any number: '))
if myNum > 0 and myNum%2 == 0:
    print('your number is an even positive number')
elif myNum > 0 and myNum%2 != 0:
    print('your number is an odd positive number')
elif myNum < 0 and myNum%2 == 0:
    print('your number is an even negative number')
elif myNum < 0 and myNum%2 != 0:
    print('your number is an odd negative number')
else:
    print('your number is 0!')