# Write a program that asks the user to enter their name in lowercase and then 
# capitalizes the first letter of each word of their name.

lst=[]
n=int(input('Enter the no. of names :'))
for i in range(n) :
    lst.append(input(('Enter the name :')).capitalize())
print(lst)
