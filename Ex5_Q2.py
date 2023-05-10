str=input('Enter the string :')
n=len(str)
count=0
for ch in str :
    if ch.isspace():
        count+=1
print('No. of characters in the string :',n-count)
