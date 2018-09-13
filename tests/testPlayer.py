from Player import Player
from Cards import shuffleCards

simon = Player("Simon", 1)
deckOfCards = shuffleCards();
simon.whoAmi()

for i in range(5):
    simon.addCard(deckOfCards[i])

print("In my hand I have:")
simon.showCards(simon.getHand())

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
