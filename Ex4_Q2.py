# a. Write a function called add_excitement that takes a list of strings and adds an exclamation 
# point (!) to the end of each string in the list. The program should modify the original list 
# and not return anything.
# b. Write the same function except that it should not modify the original list and should 
# instead return a new list.

strings=list(eval(input('Enter the list of strings :')))
n=len(strings)
def add_excitement(strings) :
    for i in range(n) :
        strings[i]+='!'
    return strings[::]
lst=add_excitement(strings)
print(lst)
