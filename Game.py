from Player import Player
from Cards import shuffleCards
"""

    A game consists of
        * a start - the setup of the game, initialising players, dealing the initial cards
        * a middle - where players take turns to play their cards and the others have to respond
        * an end - where one player declares victory based on the criteria

"""

numOfPlayers = input("How many players? : ")

"""
    THIS IS THE START - Initialise the game
"""

# DONE Mia Homework: Create the start of the game whereby we initialise the players
# Create an array to store the Players
players = []

for position in range(1, int(numOfPlayers) + 1):
    playerName = input("What is the name of player %d: " % position)
    player = Player(playerName, position)
    players.append(player)

# Next need to create a deck, with the shuffled cards
shuffledDeck = shuffleCards()

# Finally need to deal 5 cards to EACH player - that might require a loop :-)
cardCounter = 0
for player in players:
    for x in range(5):
        player.addCard(shuffledDeck[cardCounter])
        cardCounter = cardCounter + 1


for player in players:
    player.whoAmi()
    player.showCards(player.getHand())

# Need a discard pile which will initially be empty
discardPile = []

"""
    THIS WILL BE THE MIDDLE - Where players take it in turns     
"""
# TODO Mia - write the code that happens in the middle of the game
'''
[STEP 1] The player whose turn it is takes 2 cards from the deck
The player then makes their move (depending on the cards they have in their hand)
Move cards could be
    bank
    property
    action
    
If an action card is played that involves other player(s) then
    Is the action for one player? 
        If so select the player
            That player has to respond
    Or ALL players?
        ALL players in turn (hint loop) have to respond

Player responses could be:
    just say no
    hand over money
    hand over properties (for actions which are steals or as monetary values)

Cards at this point move from one player(s) to the player whose go it is
Depending on the card played, it could go into the discard pile on the table

Play then moves onto next player and go back to [STEP 1] 
  
'''
"""
    THIS WILL BE THE END - Where someone declares victory!
"""
