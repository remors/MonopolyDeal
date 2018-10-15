'''
consists of (attributes)
    player name - who is it!
    order of play - order in game play i.e. 1 goes first and after the last order
    bank pile - where money and action cards effectively only have a monetary value to pay off other players
    property cards - property sets
    hand - cards ready to play

actions (your turn) (methods)
    Take 2 cards from the shuffled deck
    Take 5 cards if you have zero cards
    Place 0-3 cards (and actions thereof)
    Declare victory!
    If you have more than 7 cards at the end of a turn you have to discard extras

actions (out of turn) (methods)
    Pay a player - from your bank pile or property pile
    Just say no! - negate a request from another player

'''

class Player():
    def __init__(self, playerName, position):
        # attributes
        self.playerName = playerName
        self.position = position
        self.bankCards = []
        self.propertyCards = []
        self.handCards = []

    # Adds a card to your hand.
    # Adding to other piles such as property or bank is done by moving a card from the hand to the pile so is a
    # different method
    def addCard(self, card):
        self.handCards.append(card)

    # Displays the cards in a pile. Could be the bank, property or hand.
    # This is where we'll add the graphics later
    def showCards(self, cardPile):
        cardNum = 1
        for card in cardPile:
            print("%d) %s" % (cardNum, card))
            cardNum = cardNum + 1

    def getHand(self):
        return self.handCards

    def getBank(self):
        return self.bankCards

    def getProperties(self):
        return self.propertyCards

    def getPlayerName(self):
        return self.playerName

    def getPosition(self):
        return self.position

    # Tells me who this object is
    def whoAmi(self):
        print("I am %s playing position %d" % (self.playerName, self.position))

    # TODO Mia - check out the next few functions and see if you can understand what they are doing. Also worth having aplay around with them in testPlayer

    # Useful for moving cards between various piles, including from one players pile to another players pile
    def moveCardBetweenPiles(self, cardNum, fromPile, toPile):
        toPile.append(fromPile[cardNum])
        fromPile.remove(fromPile[cardNum])

    # Move a card from my hand to the bank (using the generic moveCardBetweenPiles method
    def bankCard(self, cardNum):
        # You can move any card except a property card so check it's not a property card
        if (self.handCards[cardNum][0][0] == 'Property'):
            print("Computer says no")
        else:
            # Move the card selected from the hand to the bank
            self.moveCardBetweenPiles(cardNum, self. handCards, self.bankCards)

    # Move a card from my hand to the property pile (using the generic moveCardBetweenPiles method
    def propertyCard(self, cardNum):
        # You can only move a property card so check it's not something else
        if (self.handCards[cardNum][0][0] == 'Property'):
            # Move the card selected from the hand to the bank
            self.moveCardBetweenPiles(cardNum, self.handCards, self.propertyCards)
        else:
            print("Computer says no")

    #TODO Mia homework: I've not tested this, can you test this please?
    def canISayNo(self):
        justSayNo = False
        for card in self.handCards:
            if card[0][1] == 'Just Say No':
                justSayNo = True
        return justSayNo


