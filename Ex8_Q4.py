a=int(input('Enter the value for a :'))
b=int(input('Enter the value for b :'))
try :
    print((a+b)/(a-b))
except ZeroDivisionError :
    print('ZeroDivisionError')