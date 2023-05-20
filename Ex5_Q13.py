# Write a program that asks the user to enter two strings of the same length. The 
# program should then check to see if the strings are of the same length. If they are 
# not, the program should print an appropriate message and exit. If they are of the same 
# length, the program should alternate the characters of the two strings. For example, 
# if the user enters abcde and ABCDE the program should print out AaBbCcDdEe

s1=input('Enter the first string :')
s2=input('Enter the second string :')
s=''
n1=len(s1)
n2=len(s2)
if n1!=n2 :
    print('Enter two strings of same length!')
else :
    for i in range(n1) :
        s+=s1[i]+s2[i]
print(s)
