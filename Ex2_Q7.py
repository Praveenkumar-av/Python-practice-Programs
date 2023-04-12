n1=int(input("Enter first number :"))
n2=int(input('Enter second number :'))
if(n2>n1) :
    temp=n1
    n1=n2
    n2=temp
while (n2!=0) :
    rem=n1%n2
    n1=n2
    n2=rem
print('GCD is',n1)