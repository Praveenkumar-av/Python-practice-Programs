lst=[]
n=int(input('Enter the no. of elements :'))
for i in range (n) :
    lst.append(int(input()))
l=lst[-1::-1]
print(l)
start=int(input('Enter the start value :'))
stop=int(input('Enter the stop value :'))
while(start<stop) :
    temp=lst[start]
    lst[start]=lst[stop]
    lst[stop]=temp
    start+=1
    stop-=1
print(lst)
