# Write a function called change_case that given a string, returns a string with each
# upper case letter replaced by a lower case letter and vice-versa.

def change_case(s) :
    s1=str()
    for i in s :
        if i.isupper() :
            s1+=i.lower()
        elif i.islower() :
            s1+=i.upper()
    return s1
s=input('Enter the string :')
s1=change_case(s)
print(s1)