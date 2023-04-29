# Given an array of numbers. You have to give the range in which each number is the maximum element.
# Example, If array is 1, 5, 4, 3, 6. The output would be
# 1 [1, 1]
# 5 [1, 4]
# 4 [3, 4]
# 3 [4, 4]
# 6 [1, 5]

lst=eval(input('Enter the array :'))
n=len(lst)
result=dict()
for i in range(n) :
    j=i+1
    while(j<n) :
        if(lst[j]>lst[i]) :
            max=j
            break
        j+=1
    else :
        max=n
    j=i-1
    while(j>=0) :
        if(lst[j]>lst[i]) :
            min=j+2
            break
        j-=1
    else :
        min=1
    result[lst[i]]=[min,max]
for i in lst :
    print(i,result[i])