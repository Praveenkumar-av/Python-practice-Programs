# Write a function called rectangle that takes two integers m and n as arguments and prints 
# out an m × n box consisting of asterisks. Shown below is the output of rectangle(2,4)
#   ****
#   ****

m=int(input('Enter m :'))
n=int(input('Enter n :'))
def rectangle(m,n) :
    for i in range(m) :
        print(n*'*')
rectangle(m,n)
