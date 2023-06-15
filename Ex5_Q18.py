# The goal of this exercise is to see if you can mimic the behavior of the in operator and
# the count and index methods using only variables, for loops, and if statements.
#   a. Without using the in operator, write a program that asks the user for a string
# and a letter and prints out whether or not the letter appears in the string.
#   b. Without using the count method, write a program that asks the user for a string
# and a letter and counts how many occurrences there are of the letter in the
# string.
#   c. Without using the index method, write a program that asks the user for a string
# and a letter and prints out the index of the first occurrence of the letter in the
# string. If the letter is not in the string, the program should say so

str=input('Enter the string :')
ch=input('Enter the letter to search :')
found=0
count=0
index=-1
for i in range(len(str)) :
    if str[i]==ch and found==0 :
        found=1
        index=i
    if str[i]==ch :
        count+=1
if found :
    print('Letter is found')
    print('Count of the letter is',count)
    print('First occurence of letter is index',index)
else :
    print('Letter is not found')