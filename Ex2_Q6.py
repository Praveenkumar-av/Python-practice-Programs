  #6. Write a program to play the following simple game. The player starts with $100. On each turn a 
 #coin is flipped and the player has to guess heads or tails. The player wins $9 for each correct guess 
 #and loses $10 for each incorrect guess. The game ends either when the player runs out of money or gets
 #to $200.

import random
score=100
while (True) :
    l=['h','t']
    coin=l[random.randint(0,1)]
    user=input("Enter your choice('h' for head and 't' for tail) :")
    if(user==coin) :
        score+=9
    else :
        score-=10
    print(score)
    if(score<=0 or score >=200) : break