# Write a program to ask the user no. of 'The Alchemist', 'Rich dad poor dad',
# and 'Harry potter' and print the total amount of the books.Also apply a discount of 15%.

q1=int(input("Enter the no. of 'The Alchemist' book :"))
q2=int(input("Enter the no. of 'Rich dad poor dad :"))
q3=int(input("Enter the no. of 'Harry potter' book:"))
b1=70
b2=120
b3=100
total=(q1*b1)+(q2*b2)+(q3*b3)
total-=total*0.15
print('Total amount =',round(total,2))
