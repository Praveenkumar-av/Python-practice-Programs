# Use the Standard_deck class of this section to create a simplified version of the 
# game War. In this game, there are two players. Each starts with half of a deck. The 
# players each deal the top card from their decks and whoever has the higher card wins 
# the other player's cards and adds them to the bottom of his deck. If there is a tie, the 
# two cards are eliminated from play (this differs from the actual game, but is simpler 
# to program). The game ends when one player runs out of cards.

lst=['A','2','3','4','5','6','7','8','9','J','Q','K']
from random import shuffle
shuffle(lst)
l1=lst[::]
shuffle(lst)
l2=lst[::]
class standard_deck :
    def __init__(self,l1,l2) :
        self.h1=l1
        self.h2=l2

    def play(self) :
        for i in range(1000) :
            if len(self.h1)==0 or len(self.h2)==0 :
                break
            else :
                if self.h1[0]==self.h2[0] :
                    del self.h1[0]
                    del self.h2[0]     
                else :
                    self.h1.append(self.h1[0])      
                    self.h2.append(self.h2[0])     
                    del self.h1[0]
                    del self.h2[0] 
            print('h1:',self.h1)
            print('h2:',self.h2)

p1=standard_deck(l1,l2)
p1.play()
if len(p1.h1)==len(p1.h2) :
    print('Draw')
elif len(p1.h1)>len(p1.h2) :
    print('Player 1 wins!')
else :
    print('Player 2 wins!')