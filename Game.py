import copy
import random
import Card
import Cardset

GameOver =  False
turn = 0
player1 = 0
player2 = 1
CurrentPlay = Cardset.CurrentPlay
Gamebank = Cardset.GameBank


Cardsett2 = []
Fullset = Cardset.fullSetOfCard

CardSett1 = []
Cardset.borrowCard(CardSett1,Gamebank,5)

Cardset.borrowCard(Cardsett2,Gamebank,5)
Cardset.borrowCard(CurrentPlay)
  
    

#def chooseOption( input):


"""
while not GameOver:
    
    
    if(turn == player1):

        currentCard = CurrentPlay[-1]
        print('the card on set is : %r %r'% (currentCard.name,currentCard.symbol))
        Cardset.printCardSet(CardSett1)
        inputCard = input("enter  which your card name and symbol: ")


        



    turn += 1
    turn = turn % 2    

"""
