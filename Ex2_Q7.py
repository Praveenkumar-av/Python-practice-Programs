  #7. The GCD (greatest common divisor) of two numbers is the largest number that both are divisible by.
 # For instance, gcd(18,42) is 6 because the largest number that both 18 and 42 are divisible by is 6. 
 #Write a program that asks the user for two numbers and computes their gcd. Shown below is a way to
 # compute the GCD, called Euclid's Algorithm.
 #  o	First compute the remainder of dividing the larger number by the smaller number
 #  o	Next, replace the larger number with the smaller number and the smaller number with the remainder.
 #  o	Repeat this process until the smaller number is 0. The GCD is the last value of the larger number.

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