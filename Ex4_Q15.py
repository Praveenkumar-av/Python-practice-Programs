# Write a function called root that is given a number x and an integer n and
# returns x1/n. In the function definition, set the default value of n to 2.

def root(x,n=2) :
    n=1/n
    return x**n
x=int(input('Enter a number :'))
n=int(input('Enter the root number :'))
print(root(x,n))