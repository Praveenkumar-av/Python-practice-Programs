# Write a class called Rock_paper_scissors that implements the logic of the game
# Rock-paper-scissors. For this game the user plays against the computer for a certain
# number of rounds. Your class should have fields for the how many rounds there will
# be, the current round number, and the number of wins each player has. There should
# be methods for getting the computer's choice, finding the winner of a round, and
# checking to see if someone has one the (entire) game. You may want more methods.

n=int(input('Enter the no. of rounds :'))
class rock_paper_scissors :
    winner=0
    def __init__(self) :
        self.round=0
        self.com=0
        self.player=0
        self.com_choice=''
        self.user_choice=''

    def choice(self) :  # computer's random choice
        from random import randint
        lst=['R','P','S']
        self.com_choice=lst[randint(0,2)]

    def play(self) :
        self.choice()
        self.round+=1
        rock_paper_scissors.winner=0
        self.user_choice=input('Enter your choice :') # user choice
        if self.user_choice==self.com_choice :
            rock_paper_scissors.winner=2
        elif self.user_choice=='R' and self.com_choice=='S' :
            self.player+=1
        elif self.user_choice=='P' and self.com_choice=='R' :
            self.player+=1
        elif self.user_choice=='S' and self.com_choice=='P' :
            self.player+=1
        else :
            self.com+=1
            rock_paper_scissors.winner=1
        self.print_winner()

    def print_winner(self) :
        if rock_paper_scissors.winner==0 :
            print(f'Winner of Round {self.round} is Player')
        elif rock_paper_scissors.winner==1 :
            print(f'Winner of Round {self.round} is Computer')
        else :
            print(f'Winner of Round {self.round} is None')

g1=rock_paper_scissors()
for i in range(n) :
    g1.play()
if g1.player==g1.com :
    print('RESULT :Game Draw')
elif g1.player>g1.com :
    print('RESULT :Player wins')
else :
    print('RESULT :Computer wins')