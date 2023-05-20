# Write a program that asks the user to enter a word and then capitalizes every other 
# letter of that word. So if the user enters rhinoceros, the program should 
# print rHiNoCeRoS.

str=input('Enter the string :')
cap=''
n=len(str)
for i in range(n) :
    if i%2==1 :
        cap+=str[i].upper()
    else :
        cap+=str[i]
print(cap)
