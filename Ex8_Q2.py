class Vote(Exception) :
    pass

age=input('Enter the age :')
try :
    a=int(age)
    if a<18 :
        raise Vote()
    else :
        print('Eligible to Vote')
except ValueError :
    print('Enter only integers!')
except Vote :
    print('You are not eligible to Vote')