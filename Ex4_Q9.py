# Write a function called factors that takes an integer and returns a list of its factors.

def factors(num) :
    lst=[]
    for i in range(1,num+1) :
        if (num%i==0) :
            lst.append(i)
    return lst
num=int(input('Enter the number :'))
lst=factors(num)
print(lst)