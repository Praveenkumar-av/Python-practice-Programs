# Given a list of integers, multiply the even integers by 3 and the odd
# integers with 5, return the sum of all the items after the
# multiplication.

lst=[]
n=int(input('Enter the no. of elements :'))
print('Enter the list :')
for i in range(n):
    lst.append(int(input()))
sum=0
for i in range(n):
    if (lst[i]%2==0) :
        sum+=(lst[i]*3)
    else :
        sum+=(lst[i]*5)
print('Sum is',sum)
