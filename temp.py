lst=['praveen','apple','banana']
target=input('Enter a word "')
def find(L, target):
    start = 0
    end = len(L) - 1

    while start <= end: 
        middle = (start + end)// 2 
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle
print(find(lst,target))