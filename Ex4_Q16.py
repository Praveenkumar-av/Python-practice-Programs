#  Write a function called one_away that takes two strings and returns True if the strings are 
# of the same length and differ in exactly one letter, like bike/hike or water/wafer.

def one_way(s1,s2) :
    n1=len(s1)
    n2=len(s2)
    i=0; count=0
    while(i<n1 and i<n2) :
        if s1[i]!=s2[i] :
            count+=1
        i+=1
    if n1==n2 and count==1 :
        return True
    return False
s1=input('Enter first string :')
s2=input('Enter second string :')
print(one_way(s1,s2))