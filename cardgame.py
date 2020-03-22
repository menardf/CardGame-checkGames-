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

        
def createCardset():
    cardset = []
    
    cardset.append(Card('ACE','spade',1)), cardset.append(Card('2','spade',2)), cardset.append(Card('3','spade',3)),
    cardset.append(Card('4','spade',4)), cardset.append(Card('5','spade',5)), cardset.append(Card('6','spade',6)),
    cardset.append(Card('7','spade',7)), cardset.append(Card('8','spade',8)), cardset.append(Card('9','spade',9)),
    cardset.append(Card('10','spade',10))
    cardset.append(Card('ACE','diamond',11)), cardset.append(Card('2','diamond',12)), cardset.append(Card('3','diamond',13)),
    cardset.append(Card('4','diamond',14)), cardset.append(Card('5','diamond',15)), cardset.append(Card('6','diamond',16)),
    cardset.append(Card('7','diamond',17)), cardset.append(Card('8','diamond',18)), cardset.append(Card('9','diamond',19)),
    cardset.append(Card('10','diamond',20))
    cardset.append(Card('ACE','clover',21)), cardset.append(Card('2','clover',22)), cardset.append(Card('3','clover',23)),
    cardset.append(Card('4','clover',24)), cardset.append(Card('5','clover',25)), cardset.append(Card('6','clover',26)),
    cardset.append(Card('7','clover',27)), cardset.append(Card('8','clover',28)), cardset.append(Card('9','clover',29)),
    cardset.append(Card('10','clover',30))
    cardset.append(Card('ACE','heart',31)), cardset.append(Card('2','heart',32)), cardset.append(Card('3','heart',33)),
    cardset.append(Card('4','heart',34)), cardset.append(Card('5','heart',35)), cardset.append(Card('6','heart',36)),
    cardset.append(Card('7','heart',37)), cardset.append(Card('8','heart',38)), cardset.append(Card('9','heart',39)),
    cardset.append(Card('10','heart',40))
    cardset.append(Card('J','spade',41)),cardset.append(Card('K','spade',42)),cardset.append(Card('Q','spade',43)),
    cardset.append(Card('J','diamond',44)),cardset.append(Card('K','diamond',45)),cardset.append(Card('Q','diamond',46)),
    cardset.append(Card('J','clover',47)),cardset.append(Card('K','clover',48)),cardset.append(Card('Q','clover',49)),
    cardset.append(Card('J','heart',50)),cardset.append(Card('K','heart',51)),cardset.append(Card('Q','heart',52)),
    cardset.append(Card('JOKER','red',53))
    cardset.append(Card('JOKER','black',54))

    return cardset

def printCardset( cardSet):
    for card in cardSet:
        print(card)


fullSetOfCard = createCardset()
random.shuffle(fullSetOfCard) # this is the full set of card for reference 
GameBank = (copy.deepcopy(fullSetOfCard)) #this is the set of card which is going to be used through the game 
CardSet1 = []
CardSet2 = []
CurrentPlay = []


def findIdn(Name ,Symbol, Cardset =fullSetOfCard):
    for card in Cardset:
        if card.name == Name.upper() and card.symbol == Symbol:
            idn = card.idn
            Card = card
    return idn, Card
       
def findCard( idn, Cardset = fullSetOfCard):
    
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

def borrowCard(ToCardSet,FromCardBank=GameBank,n = 1):
    
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

def Ispenalty(playedcard, currentcard):
    if playedcard.name == '7':
        return 2
    if playedcard.name == 'JOKER':
        return 4


def IsValidPlay(idn, theCurrentplay= CurrentPlay):
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
    


def playCard(idn ,FromCardSet , ToCardset):
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
