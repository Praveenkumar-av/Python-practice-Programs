  #Write a Python program that will: 
 # o	Ask the user for seven numbers
 # o	Print the total sum of the numbers
 # o	Print the count of the positive entries, the number entries equal to zero, and the number of negative entries. Use an if, elif, else chain, not just three if statements.

num=[]
print('Enter seven integers :')
for i in range(7) :
    num.append(int(input()))
sum=0
positive=0
negative=0
zero=0
for i in range(7) :
    sum+=num[i]
    if(num[i]>0) : positive+=1
    elif (num[i]<0) : negative+=1
    else : zero+=1
print("Sum =",sum)
print('Positive entries count :',positive)
print('Negative entries count :',negative)
print('Number equal to zero :',zero)
