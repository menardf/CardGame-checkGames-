import copy
import random
import sys
from Card import Card


def createCardSet():  #create a set of 54 cards objects 
    cardset = []
    
    cardSymbol = ['spade', 'diamond', 'heart', 'clover']
    cardName = ['ACE','2', '3', '4', '5', '6', '7' ,'8' ,'9','10','J', 'K', 'Q']
    cardID=1

    for cName in cardName :
        for cSymbol in cardSymbol :
            cardset.append(Card(cName,cSymbol,cardID))
            cardID+=1
    cardset.append(Card('JOKER','red',53))
    cardset.append(Card('JOKER','black',54))
    return cardset

def printCardSet( cardSet): #print a set of card 
    for card in cardSet:
        print(card)


fullSetOfCard = createCardSet()
random.shuffle(fullSetOfCard) # this is the full set of card for reference 
GameBank = (copy.copy(fullSetOfCard)) #this is the set of card which is going to be used through the game 
CardSet1 = []
CardSet2 = []
CurrentPlay = []

def findIdn(Name ,Symbol, Cardset =fullSetOfCard): #find the id number of a given symbol and name 
    Idn = None
    Card = None
    for card in Cardset:
        if card.name == Name.upper() and card.symbol == Symbol:
            Idn = card.idn
            Card = card
    if not Idn:
        return 'your card is not in this set'
    
    return Idn, Card
       
def findCard( idn, Cardset = fullSetOfCard): #find the symbol and name of a given id in a card set 
    
    Name = None
    symbol = None
    for card in Cardset:
        if card.idn == idn:
            Name = card.name
            symbol = card.symbol
            Card = card
    
    if not Name :
        return 'your card is not in this set'
        
    #print('Card(%r,%r)'%(Name,symbol))
    return Name,symbol

def borrowCard(ToCardSet,FromCardBank=GameBank,n = 1): #borrow one or more  random card from a card set and add them  to another card set 
    lent = len(FromCardBank)    
    randomNumber = random.randint(0,lent-1)
    if n==1 : 
        borrowedCard = FromCardBank[randomNumber ]
        ToCardSet.append(borrowedCard)
        FromCardBank.pop(randomNumber)
        return borrowedCard
    elif n>1 :
        i = 1
        while i<=n :
            
            borrowedCard = FromCardBank[ random.randint(0,len(FromCardBank)-1)]
            ToCardSet.append(borrowedCard)
            FromCardBank.remove(borrowedCard)
            i+=1
        return ToCardSet

def IsSpecial(Idn ): #determine if there is a panalty associated to a played card and return the number of cards to be borrowed 
    name = findCard(Idn)[0]
    effect = None
    if name == '7':
        effect = 2
    if name == 'JOKER':
        effect = 4
    if name == 'J':
        effect = 'changeColor'
    if name == 'A':
        effect = 'skip'
    return effect 

#def applyEffect(effect , TocardSet)

def IsValidPlay(idn, theCurrentplay= CurrentPlay): #determine if the card choosen by a player constitute a valid play 
    currentcard = theCurrentplay[-1]
    name = findCard(idn)[0] 
    symbol = findCard(idn)[1]
    if name == currentcard.name or symbol == currentcard.symbol :
        return True 
    
    if name == 'JOKER' and symbol == 'black' and (currentcard.symbol == 'spade' or currentcard.symbol == 'clover'):
        return True
    
    if name == 'JOKER' and symbol == 'red' and (currentcard.symbol == 'heart' or currentcard.symbol == 'diamond'):
        return True
    
    if name == 'J' :
        return True 
    
    if (symbol == 'spade' or symbol == 'clover') and currentcard.name == 'JOKER' and currentcard.symbol == 'black':
        return True 
    
    if (symbol == 'heart' or symbol == 'diamond') and currentcard.name == 'JOKER' and currentcard.symbol == 'red':
        return True
    
    if name == '2':
        return True 
    return False

def playCard(idn ,FromCardSet , ToCardset=CurrentPlay):  # remove a specific card from a card set and add it to another card set 
    removedCard = None
    for card in FromCardSet:
        if card.idn == idn:
            card.removeCard(FromCardSet)
            removedCard = card
            removedCard.addCard(ToCardset)

    printCardSet(FromCardSet) 

def winningState(CardSet1=CardSet1,CardSet2= CardSet2):
    win = None
    if len(CardSet1)==0:
        win = 'player 1'
        
    elif len(CardSet2) == 0:
        win = 'player 2 '

    return win

#***********************************driver code *********************************

GameOver = False
turn = 0
player1 = 0
player2 = 1



def chooseOption(Cardset,TocardSet = CurrentPlay):
    option = int(input('press 1 to see your card set and 2 to play your next move : '))
    if option == 1:
        printCardSet(CardSet1)
        option = 2
        
    if option == 2:
        choosenCname = input('chose a card name (A-2-10-J-Q-K) :')
        choosenCsymbol = input('chose a card symbol (spade,diamond,clover,heart) :')
        choosenCidn = findIdn(choosenCname,choosenCsymbol)[0]
        if IsValidPlay(choosenCidn):
            if not IsSpecial(choosenCidn):
                print('')
                playCard(choosenCidn,Cardset)

            else :
                effect = IsSpecial(choosenCidn)


borrowCard(CardSet1,GameBank,5)
borrowCard(CardSet2,GameBank,5)
borrowCard(CurrentPlay)

while not GameOver:
    
    if(turn == player1):

        currentCard = CurrentPlay[-1]
        print('the card on set is : %r %r'% (currentCard.name,currentCard.symbol))
        chooseOption(CardSet1)
            
        

    else:    
        currentCard = CurrentPlay[-1]
        print('the card on set is : %r %r'% (currentCard.name,currentCard.symbol))
        chooseOption(CardSet2)
        GameOver = True

    turn += 1
    turn = turn % 2    