num=input('Enter the Value in Celsius :')
try :
    c=float(num)
    f=(c*(9/5))+32
    print('Fahrenheit :{:.2f}'.format(f))
except ValueError :
    print('Invalid input')
