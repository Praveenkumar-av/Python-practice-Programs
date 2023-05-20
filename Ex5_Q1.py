# Write a program that asks the user to enter a string. The program should then print 
# the following:
# a. The total number of characters in the string
# b. The string repeated 10 times
# c. The first character of the string (remember that string indices start at 0)
# d. The first three characters of the string
# e. The last three characters of the string
# f. The string backwards
# g. The seventh character of the string if the string is long enough and a message 
#    otherwise
# h. The string with its first and last characters removed
# i. The string in all caps
# j. The string with every a replaced with an e
# k. The string with every letter replaced by a space

str=input('Enter the string :')
n=len(str)
count=0
str1=''  # string replaced with e
for ch in str:
    if ch.isspace():
        count+=1
if n>0 :
    print('The no. of characters in the string :',n-count)
    print('First character in the string :',str[0])
    print('First Three character of the string :',str[0]+str[1]+str[2])
    print('Last Three characters of the string :',str[n-3]+str[n-2]+str[n-1])
    print('String Backwards :',str[-1::-1])
    if n>6 :
        print('Seventh character of the string :',str[6])
    print('String with First and Last character removed :',str[1:n-1:1])
    print('String in all Caps :',str.upper())
    for ch in str :
        if ch=='a' :
            str1+='e'
        else :
            str1+=ch
    print("String with 'a' replaced by 'e' :",str1)
    for ch in str :
        if not(ch.isspace()):
            print(' ',ch,end='')
else :
    print('Please Enter a string !')
            
