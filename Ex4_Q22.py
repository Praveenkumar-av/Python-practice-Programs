lst=list(eval(input('Enter the list of strings :')))
find=input('Enter the word to find :')
def binary_search(lst,find) :
    low=0
    up=len(lst)-1
    mid=(low+up)//2
    while low<up :
        r=find==lst[mid]
        if r==0 :
            return mid
        elif r<0 :
            