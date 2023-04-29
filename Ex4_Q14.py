#  Write a function called is_sorted that is given a list and returns True if the list is
# sorted and False otherwise.

def is_sorted(l) :
    lst=l[::]
    n=len(lst)
    i=0
    j=0
    while i<n :
        j=i+1
        while j<n :
            if lst[j]<lst[i] :
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
            j+=1
        i+=1
    i=0
    while i<n :
        if lst[i]!=l[i] :
            return False
        i+=1
    return True
l=list(eval(input('Enter the list :')))
result=is_sorted(l)
print(result)