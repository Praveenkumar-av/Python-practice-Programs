# A simple way to estimate the number of words in a string is to count the number of 
# spaces in the string. Write a program that asks the user for a string and returns an 
# estimate of how many words are in the string.

str=input('Enter the string :')
n=len(str)
count=0
for ch in str :
    if ch.isspace():
        count+=1
print('No. of characters in the string :',n-count)
