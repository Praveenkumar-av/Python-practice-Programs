# Ask the user for a number and then print the following, where the pattern ends at the 
# number that the user enters.
# 1
#  2
#   3
#    4

num=input('Enter a number :')
space=''
for i in num :
    print(space+i)
    space+=' '
