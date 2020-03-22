import copy
import random

class Card:
    def __init__(self,name,symbol,idn):
        self.name = name
        self.symbol = symbol
        self.idn = idn
    
    def __str__(self):
        return "Card(%r,%r)"%(self.name,self.symbol)
    
    def addCard(self, CardSet):
        CardSet.append(Card(self.name,self.symbol,self.idn))

    
    def removeCard(self, CardSet):
        for card in CardSet:
            if card.idn == self.idn:
                CardSet.remove(card)

        
def createCardset():  #create a set of 54 cards objects 
    cardset = []
    cardSymbol = ['spade', 'diamond', 'heart', 'clover']
    cardName= ['ACE' '2', '3', '4', '5', '6', '7' ,'8' ,'9', 'J', 'K', 'Q']
    cardID=1
    
    for cType in cardSymbol:
        for cSymbol in cardName:
            cardset.append(Card(cSymbol,cType,cardID))
            cardID+=1
    
    cardset.append(Card('JOKER','red',53))
    cardset.append(Card('JOKER','black',54))

    return cardset

def printCardset( cardSet): #print a set of card 
    for card in cardSet:
        print(card)


fullSetOfCard = createCardset()
random.shuffle(fullSetOfCard) # this is the full set of card for reference 
GameBank = (copy.deepcopy(fullSetOfCard)) #this is the set of card which is going to be used through the game 
CardSet1 = []
CardSet2 = []
CurrentPlay = []


def findIdn(Name ,Symbol, Cardset =fullSetOfCard): #find the id number of a given symbol and name 
    for card in Cardset:
        if card.name == Name.upper() and card.symbol == Symbol:
            idn = card.idn
            Card = card
    return idn, Card
       
def findCard( idn, Cardset = fullSetOfCard): #find the symbol and name of a given id in a card set 
    
    Name = None
    symbol = None
    for card in Cardset:
        if card.idn == int(idn):
            Name = card.name
            symbol = card.symbol
            Card = card
    if not Name :
        return "your card is not in this set"
        
    print("Card(%r,%r)"%(Name,symbol))
    return Name,symbol,Card

def borrowCard(ToCardSet,FromCardBank=GameBank,n = 1): #borrow one or more  random card from a card set and add them  to another card set 
    
    if n==1 :
        randomNumber = random.randint(0,len(FromCardBank)-1)
        borrowedCard = FromCardBank[randomNumber ]
        ToCardSet.append(borrowedCard)
        FromCardBank.pop(randomNumber)
        return borrowedCard
    elif n>1 :
        i = 1
        while i<=n :
            randomNumber = random.randint(0,len(FromCardBank)-1)
            borrowedCard = FromCardBank[randomNumber ]
            ToCardSet.append(borrowedCard)
            FromCardBank.pop(randomNumber)
            i+=1
        return ToCardSet

def Ispenalty(playedcard, currentcard): #determine if there is a panalty associated to a played card and return the number of cards to be borrowed 
    if playedcard.name == '7':
        return 2
    if playedcard.name == 'JOKER':
        return 4


def IsValidPlay(idn, theCurrentplay= CurrentPlay): #determine if the card choosen by a play constitute a valid play 
    currentcard = theCurrentplay[-1]
    playedcard = findCard(idn)[2]
    if playedcard.name == currentcard.name or playedcard.symbol == currentcard.symbol :
        return True 
    
    if playedcard.name == 'JOKER' and playedcard.symbol == 'black' and (currentcard.symbol == 'spade' or currentcard.symbol == 'clover'):
        return True
    
    if playedcard.name == 'JOKER' and playedcard.symbol == 'red' and (currentcard.symbol == 'heart' or currentcard.symbol == 'diamond'):
        return True
    
    if playedcard.name == 'J' :
        return True 
    
    if (playedcard.symbol == 'spade' or playedcard.symbol == 'clover') and currentcard.name == 'JOKER' and currentcard.symbol == 'black':
        return True 
    
    if (playedcard.symbol == 'heart' or playedcard.symbol == 'diamond') and currentcard.name == 'JOKER' and currentcard.symbol == 'red':
        return True
    
    if playedcard.name == '2':
        return True 
    


    
borrowCard(CardSet1,GameBank,5)
borrowCard(CardSet2,GameBank)
print(len(GameBank))
    


def playCard(idn ,FromCardSet , ToCardset):  # remove a specific card from a card set and add it to another card set 
    for card in FromCardSet:
        if card.idn == idn:
            card.removeCard(FromCardSet)
            removedCard = card
    removedCard.addCard(ToCardset)



printCardset(CardSet1) 
print('')
printCardset(CardSet2)
#ayee = findIdn('k','spade')[1]
#print(ayee)
#ayee.removeCard(GameBank)
#print(findCard(ayee.idn,GameBank))
