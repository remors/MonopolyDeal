from Player import Player
from Cards import shuffleCards
import Actions as Actions

simon = Player("Simon", 1)
mia = Player("Mia",2)
fred = Player("Fred",3)

deckOfCards = shuffleCards();
simon.whoAmi()
mia.whoAmi()
fred.whoAmi()

#Test moveCardBetweenPiles
for i in range(5):
    simon.addCard(deckOfCards[i])
    mia.addCard(deckOfCards[i+5])

print("Simon has in his hand")
simon.showCards(simon.getHand())
print("Mia has in her hand")
mia.showCards(mia.getHand())

#This tests moveCardBetweenPiles
"""
cardNum = input("Pick a card to from Simon to Mia :")
simon.moveCardBetweenPiles(int(cardNum) - 1, simon.getHand(), mia.getHand())
print("Simon has in his hand")
simon.showCards(simon.getHand())
print("Mia has in her hand")
mia.showCards(mia.getHand())
"""

# TODO - [1] Mia play around with the below commented calls to see what they do
"""
cardNum = input("Pick a card to move to the bank :")
simon.bankCard(int(cardNum) - 1) # Remember position 0!

print("In my hand I have:")
simon.showCards(simon.getHand())
print("In the bank I have:")
simon.showCards(simon.getBank())

cardNum = input("Pick a card to move to the property pile :")
simon.propertyCard(int(cardNum) - 1) # Remember position 0!

print("In my hand I have:")
simon.showCards(simon.getHand())
print("In the property pile I have:")
simon.showCards(simon.getProperties())
"""
"""
print("In Simon hand I have:")
simon.showCards(simon.getHand())
print("In Mia hand I have:")
simon.showCards(mia.getHand())
cardNum = input("Pick a card to move from Simon to Mia :")
Actions.moveCardFromPlayerToPlayer(simon.getHand(), mia.getHand(), int(cardNum) - 1) # Remember position 0!
print("In Simon hand I have:")
simon.showCards(simon.getHand())
print("In Mia hand I have:")
simon.showCards(mia.getHand())
"""
