# Write a function called matches that takes two strings as arguments and returns how
# many matches there are between the strings. A match is where the two strings have
# the same character at the same index. For instance, 'python' and 'path' match in
# the first, third, and fourth characters, so the function should return 3.

def matches(s1,s2) :
    n1=len(s1)
    n2=len(s2)
    count=0
    i=0
    while(i<n1 and i<n2) :
        if(s1[i]==s2[i]) :
            count+=1
        i+=1
    return count
str1=input('Enter the first string :')
str2=input('Enter the second string :')
print(matches(str1,str2))