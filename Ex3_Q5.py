  #5. Create a list of n elements, process the elements based on the
 #following condition:
 #if element(x) is a prime number, then print x*x
 #else print the sum of digits in the number

lst=[]
n=int(input('Enter no. of elements :'))
print('Enter the elements :')
sum=0
count=0
for i in range (n) :
    lst.append(int(input()))
for j in range (n) :
    num=lst[j]
    k=2
    flag=0
    if (num==0 or num==1) : 
        print('1')
        j+=1
        continue
    while (k<num//2) :
        if(lst[j]%k==0) :
            flag=1
            break
        k+=1
    if(flag==0) :
        print(lst[j]*lst[j])
    elif (flag==1) :
        count=0
        sum=0
        num=lst[j]
        while(num!=0) :
            rem=num%10
            sum+=rem
            num//=10
        print(sum)
    j+=1