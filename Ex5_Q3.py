# People often forget closing parentheses when entering formulas. Write a program that 
# asks the user to enter a formula and prints out whether the formula has the same 
# number of opening and closing parentheses.

f=input('Enter the Forula :')
open=0
close=0
for ch in f :
    if ch=='(' :
        open+=1
    elif ch==')' :
        close+=1
if open==close :
    print('Yes')
else :
    print('No')
