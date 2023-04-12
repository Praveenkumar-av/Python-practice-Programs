w=int(input('Enter the width :'))
h=int(input('Enter the height :'))
num=0
for i in range(0,w) :
    for j in range(0,h) :
        print(num%10,end=' ')
        num+=1
    print('\n')