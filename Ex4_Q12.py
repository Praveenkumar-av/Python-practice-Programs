#  Recall that if s is a string, then s.find('a') will find the location of the first a in s.
# The problem is that it does not find the location of every a. Write a function
# called findall that given a string and a single character, returns a list containing all
# of the locations of that character in the string. It should return an empty list if there
# are no occurrences of the character in the string.

def findall(str,ch) :
    n=len(str)
    lst=[]
    for i in range(n) :
        if(str[i]==ch) :
            lst.append(i)
    return lst
str=input('Enter the string :')
ch=input('Enter the character :')
lst=findall(str,ch)
print(lst)