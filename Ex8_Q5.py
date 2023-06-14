class NegativeAge(Exception) :
    pass
age=int(input('Enter the age :'))
try :
    if age<0 :
        raise NegativeAge()
    else :
        print('Valid Age')
except NegativeAge :
    print('Age Invalid Exception')