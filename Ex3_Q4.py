  #4. Given a list which contains values as 0 and 1, process and find the
 #lengths of the group of consecutive 1's in the input list, in the order
 #from left to right.
 #Example: If the input list contains [1,1,0,1,0,0,1,1,1,0,0], then the
 #script should print [2,1,3]

lst=eval(input('Enter the list of elements :'))
i=0
n=len(lst)
result=[]
while(i<n) :
    if(lst[i]==1) :
        count=1
        j=i+1
        while(j<n and lst[j]!=0) :
            count+=1
            j+=1
        result.append(count)
        i=j
    else : i+=1
print(result)