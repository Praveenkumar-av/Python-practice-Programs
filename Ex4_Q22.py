# In the chapter on text files, the way we checked to see if a word w was a real word
# was:
# if w in words:
# where words was the list of words generated from a wordlist. This is unfortunately
# slow, but there is a faster way, called a binary search. To implement a binary search
# in a function, start by comparing w with the middle entry in words. If they are equal,
# then you are done and the function should return True. On the other hand,
# if w comes before the middle entry, then search the first half of the list. If it comes
# after the middle entry, then search the second half of the list. Then repeat the
# process on the appropriate half of the list and continue until the word is found or
# there is nothing left to search, in which case the function short return False.
# The < and > operators can be used to alphabetically compare two strings.

lst=list(eval(input('Enter the list of strings :')))
find=input('Enter the word to find :')

def binary_search(lst,find) :
    low=0
    up=len(lst)
    while low<=up :
        mid=((low+up)//2)
        if lst[mid]==find :
            return mid
        elif find<lst[mid] :
            up=mid-1
        else :
            low=mid+1
    else :
        return -1

index=binary_search(lst,find)
if index==-1 :
    print('Word not found')
else :
    print('Index :',index)