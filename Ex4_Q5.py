# Write a function called first_diff that is given two strings and returns the first location 
# in which the strings differ. If the strings are identical, it should return -1.

def first_diff(s1,s2) :
    n1=len(s1)
    n2=len(s2)
    i=0
    while(i<n1 and i<n2) :
        if not(s1[i]==s2[i]) :
            return i
        i+=1
    else :
        if (i==n1 and i==n2):
            return -1
        else :
            return i
str1=input('Enter the first string :')
str2=input('Enter the second string :')
index=first_diff(str1,str2)
print('Index :',index)
