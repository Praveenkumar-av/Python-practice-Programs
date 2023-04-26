# Write a function called sum_digits that is given an integer num and returns the sum
# of the digits of num.

num=int(input('Enter a number :'))
def sum_digits(n) :
    sum=0
    rem=0
    while n :
        rem=n%10
        sum+=rem
        n//=10
    return sum
print(sum_digits(num))
