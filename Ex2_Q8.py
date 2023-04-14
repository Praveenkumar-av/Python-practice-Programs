  #8. Write a program that draws “modular rectangles” like the ones below. The user specifies the 
 #width and height of the rectangle, and the entries start at 0 and increase typewriter fashion from 
 #left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5 rectangle and a 4 × 8.
 #w=int(input('Enter the width :'))
 #h=int(input('Enter the height :'))

num=0
for i in range(0,w) :
    for j in range(0,h) :
        print(num%10,end=' ')
        num+=1
    print('\n')