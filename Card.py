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

        




