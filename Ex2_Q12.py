  #12. Write a program that plays rock, paper, scissors: 
 # o	Create a program that randomly prints 0, 1, or 2.
 # o	Expand the program so it randomly prints rock, paper, or scissors using if statements.
 #      Don't select from a list, as shown in the chapter.
 # o	Add to the program so it first asks the user their choice.
 # o	(It will be easier if you have them enter 1, 2, or 3.)

import random
for i in range (10) :
    r=int(input('Enter your choice(1,2,3) :'))
    if(r==1) :user='Rock'
    elif(r==2) :user="Paper"
    elif(r==3) :user='Scissor'
    r=random.randint(0,2)
    if(r==0) :com='Rock'
    elif(r==1) :com="Paper"
    else :com='Scissor'
    print("Computer's choice :",com)
    print('Your choice :',user)