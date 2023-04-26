# Write a function that takes an integer n and returns a random integer with exactly n digits.
# For instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not 
# because that is really 93, which is a two-digit number.

n=int(input('Enter the no. of digits :'))
from random import randint
def random(n) :
    return randint(pow(10,n-1),pow(10,n))
print(random(n))