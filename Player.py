'''
consists of (attributes)
    player name - who is it!
    order of play - order in game play i.e. 1 goes first and after the last order
    bank pile - where money and action cards effectively only have a monetary value to pay off other players
    property cards - property sets
    hand - cards ready to play

actions (your turn) (methods)
    Take 2 cards
    Take 5 cards if you have zero cards
    Place 0-3 cards (and actions thereof)
    Declare victory!
    If you have more than 7 cards at the end of a turn you have to discard extras

actions (out of turn) (methods)
    Pay a player - from your bank pile or property pile
    Just say no! - negate a request from another player

'''

class Player():
    #attributes
    playerName = ""
    position = 0
    bankCards = []
    propertyCards = []
    handCards = []

    def __init__(self):
        pass

    def addCard(self, card):
        self.handCards.append(card)

    def showCards(self, cards):
        for card in cards:
            print(card)

    def getHand(self):
        return self.handCards


