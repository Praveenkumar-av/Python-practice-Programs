# Given an array of positive and negative integers {-1,6,9,-4,-10,-9,8,8,4} (repetition allowed) sort
# the array in a way such that the starting from a positive number, the elements should be arranged
# as one positive and one negative element maintaining insertion order. First element should be
# starting from positive integer and the resultant array should look like {6,-1,9,-4,8,-10,8,-9,4}

lst=eval(input('Enter the number :'))
lst1,lst2=[],[]
for i in lst :
    if(i>=0) :
        lst1.append(i)
    else :
        lst2.append(i)
n1=len(lst1)
n2=len(lst2)
lst=[]
i=0
while(i<n1 or i<n2) :
    if (i<n1) :
        lst.append(lst1[i])
    if (i<n2) :
        lst.append(lst2[i])
    i+=1
del lst1
del lst2
print(lst)