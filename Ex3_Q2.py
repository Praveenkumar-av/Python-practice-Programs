# Find the "centered" average of elements in a list which is mean
# average of elements except the smallest and the largest element in
# the list. If there are multiple copies of smallest (or) largest element,
# ignore only one copy of the element during computation.
# Example: [2,1,3,4,1,2,4]
# "centered" average = (1 + 2 + 2 + 3+ 4) / 5 = 2.4

lst=[]
n=int(input('Enter the no. of elements :'))
for i in range(n) :
    lst.append(int(input()))
lst.sort()
sum=0
for i in range(1,n-1) :
    sum+=lst[i]
average=sum/(n-2)
print('Centered average :',average)
