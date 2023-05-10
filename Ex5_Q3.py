f=input('Enter the Forula :')
open=0
close=0
for ch in f :
    if ch=='(' :
        open+=1
    elif ch==')' :
        close+=1
if open==close :
    print('Yes')
else :
    print('No')
