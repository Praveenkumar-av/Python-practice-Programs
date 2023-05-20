str=input('Enter the string :')
lst=str.split()
print(lst)
d=dict()
for w in lst :
    d[lst.count(w)]=w
max=0
for num in d.keys() :
    if num>max :
        max=num
print(d[max])