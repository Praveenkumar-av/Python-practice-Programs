  #11. random guesser
 #Allow the user to guess for a number. If the user finds the number within max number of tries, he wins the game.
 #After each try, the system can provide hint to aid the user in the next guess. It can print either 
 #lower (or) higher depending on the whether the guess was lower than the number (or) higher than the number.
 #Refine the code so that number of hints are increased to 4 namely ‘higher’, ‘much higher’, ‘lower’,
 #‘much lower’. If the absolute difference between the guess and the number is greater than 10 

num=56
flag=0
for i in range(10) :
    user=int(input('Enter a number :'))
    if(num==user) :
        print('You Win!')
        flag=1
        break
    elif (user<num) :
        if(abs(user-num)<=10) :
            print('Lower')
        else :
            print("Much Lower")
    else :
        if (abs(user-num<=10)) :
            print('Higher')
        else :
            print('Much higher')
if(flag==0) :
    print('You Lost!')