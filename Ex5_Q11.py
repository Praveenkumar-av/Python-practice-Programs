# Write a program that asks the user to enter a word that contains the letter a. The 
# program should then print the following two lines: On the first line should be the part 
# of the string up to and including the first a, and on the second line should be the rest 
# of the string. Sample output is shown below:
# Enter a word: buffalo
# buffa
# lo

str=input('Enter the string :')
a=str.find('a')
if a==-1 :
    print('a not found')
else :
    print(str[0:a+1])
    print(str[a+1:])
