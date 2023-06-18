# Write a function called verbose that, given an integer less than 10^15, returns the
# name of the integer in English. As an example, verbose(123456) should
# return one hundred twenty-three thousand, four hundred fifty-six.

def verbose(num) :
    s=''
    one_digit=['','one','two','three','four','five','six','seven','eight','nine']
    two_digit=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']
    if 0<num<1000 :
        if 100<=num<1000 :
            s=one_digit[num//100]+' hundred '
            num=num%100
            if num>0 :
                s+='and '
        if 0<num<100 :
            if num<10 :
                s+=one_digit[num]
            elif 10<=num<=19 :
                s+=two_digit[num%10]
            elif 19<num<100 :
                s+=tens[(num//10)-2]
                s+=one_digit[num%10]
    else :
        print('Enter only positive numbers less than 1000')
    return s

n=int(input('Enter a number less than 1000 :'))
print(verbose(n))