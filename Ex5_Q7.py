# Write a program that asks the user to enter a word and determines whether the word 
# is a palindrome or not. A palindrome is a word that reads the same backwards as 
# forwards.

s=input('Enter a string :')
rev_s=s[-1::-1]
if s==rev_s :
    print('Palindrome')
else :
    print('Not Palindrome')
