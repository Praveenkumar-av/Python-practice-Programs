  #8. Given a tuple of n integers, iteratively form tuples which records the absolute difference between 
 # the neighbouring integers. Find the exact number of steps the tuple takes to reach either tuple of 
 # all zeros (or) original tuple sequence.
 #Example: Input tuple = (1,2,1,2,1,0)
 # In the first iteration we get a new tuple of form (1,1,1,1,1,1). In the next iteration 
 # we get (0,0,0,0,0,0). It takes two steps for the tuple to reach all zeros.
 # Note: Not all tuples will descend to zeros. So, limit the number of iterations to 100. If it does 
 # not end up with input sequence or all zeros with the specified number of iterations, print 'Invalid Tuple'

tpl=eval(input('Enter the tuple :'))
n=len(tpl)
print(n)
diff=[]
count=0
lst=list(tpl)
for i in range(100) :
    flag=0
    for j in range(n-1) :
        diff.append(abs(lst[j]-lst[j+1]))
        if (j==n-2) :
            diff.append(abs(lst[j]-lst[j+1]))
        count+=1
    print(diff)
    for j in range(n) :
        if(diff[j]!=0) : flag=1
    if (flag==0) :
        break
    else :
        lst=diff
print(diff)