#  1. Given a string S, consisting of only ‘*’ and ‘|’ where ‘*’ means existence of an item and a
# ‘|’ means compartment. The number of asterisk between a pair of ‘|’ is the number of items
# in the compartment. Write a program to receive the start and end index from the user and
# identify the number of compartments within the indices [inclusive of start and end index]
# and the number of items in each compartment.
# Example:
# S = |***|*|**|*
# Start index: 0
# End Index: 7
# Output:
# Number of Compartments: 2
# Number of Items 1st Compartment: 3
# Number of Items in 2nd Compartment: 1

S=input('Enter the string :')
start=int(input('Enter start index :'))
end=int(input('Enter the end index :'))
count=0
comp=0
items=[]
for i in range(start,end) :
    if (S[i]=='|') :
        if (count>0) :
            comp+=1
            items.append(count)
            count=0
    elif (S[i]=='*') :
        count+=1
print('Number of Compartments :',comp)
i=1
for count in items :
    print('Number of items compartment {}: {}'.format(i,count))
    i+=1