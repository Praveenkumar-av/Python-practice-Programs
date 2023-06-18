# Write a function called merge that takes two already sorted lists of possibly different
# lengths, and merges them into a single sorted list.
# a. Do this using the sort method.
# b. Do this without using the sort method.

def merge1(l1,l2) :  # using sort method 
    l=l1+l2
    l.sort()
    return l

def merge2(l1,l2) :  # without using sort method 
    l=l1+l2
    n=len(l)
    for i in range(n) :
        for j in range(i+1,n) :
            if l[j]<l[i] :
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
    return l

l1=list(eval(input('Input the list 1 :')))
l2=list(eval(input('Enter the list 2 :')))
print('Sorted using sort method :',merge1(l1,l2))
print('Sorted without using sort method :',merge2(l1,l2))