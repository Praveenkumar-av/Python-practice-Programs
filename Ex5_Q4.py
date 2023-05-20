# Write a program that asks the user to enter a word and prints out whether that word 
# contains any vowels.

str=input('Enter the string :')
for ch in str :
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
        print('The string contains Vowels!')
        break
else :
    print("The string doesn't contain vowels!")
