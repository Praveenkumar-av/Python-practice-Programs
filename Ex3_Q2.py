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
