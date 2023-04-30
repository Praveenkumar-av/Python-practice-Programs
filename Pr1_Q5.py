# Given a binary array {0,1,1,0,0,1,0,0,1} , sort the array in a way that all zeros come to the left and
# all the one's come to the right side of the array.

lst=list(eval(input('Enter the binary number list :')))
zero=0
one=0
for i in lst :
    if i==0 :
        zero+=1
    elif i==1 :
        one+=1
lst=[]
for i in range(zero) :
    lst.append(0)
for i in range(one) :
    lst.append(1)
print(lst)