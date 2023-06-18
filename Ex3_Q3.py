# State the inbuilt function for reversing a list.
# Write a script to reverse a list of given elements without using built-
# in function. Ex: For a list with three elements [18,34,27], the
# reversed list is [27,34,18]
# Extend the same script by accepting two integers start and stop
# whose values are between 0 and n-1 where n is the length of the list
# and reverse only the portion of numbers between the index locations
# start and stop.
# Ex: For a list with five elements [18,34,27,45,16], start=1 and
# stop=3, then the script should print [18,45,27,34,16].

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
