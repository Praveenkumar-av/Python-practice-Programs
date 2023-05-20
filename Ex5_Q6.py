# Write a program that asks the user to enter a string s and then converts s to lowercase, 
# removes all the periods and commas from s, and prints the resulting string.

str=input('Enter the string :')
strnew=''
for ch in str :
    if not(ch=='.' or ch==',') :
        strnew+=ch.lower()
print(strnew)
