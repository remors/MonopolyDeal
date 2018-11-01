from random import shuffle

# TODO: Do we need these or shall we jsut clean them up? Should be able to infer all colours from the properties
#       dictionary structure below and the card Types from the create deck below too

#cardType = ('Sly Deal', 'Pass Go', 'Wild Card', 'Rent', 'Deal Breaker', 'Money', 'Property', 'Hotel', 'Debt Collector',
#            'House', 'Double The Rent', 'Just Say No', 'Forced Deal', 'It\'s My Birthday')
#print(cardType[4])

#colours = ('Brown', 'Cyan', 'Magenta', 'Orange', 'Red', 'Yellow', 'Green', 'Blue', 'Black', 'White', 'ALL')
#print(colours[7: 10])

# Colour : (names of properties),
#           value to buy,
#           (rental amount)
properties = {'Brown': (("Old Kent Road", "Whitechapel"),
                        1,
                        (1, 2)),
              'Cyan': (("The Angel Islington", "Euston Road", "Pentonville Road"),
                       1,
                       (1, 2, 3)),
              'Magenta': (("Pall Mall", "Whitehall", "Northumberland Avenue"),
                          2,
                          (1, 2, 4)),
              'Orange': (("Vine Street", "Marlborough Street", "Bow Street"),
                         2,
                         (1, 3, 5)),
              'Red': (("The Strand", "Fleet Street", "Trafalgar Square"),
                      3,
                      (2, 4, 6)),
              'Yellow': (("Leicester Square", "Coventery Steet", "Piccadilly"),
                         3,
                         (2, 4, 6,)),
              'Green': (("Regent Street", "Oxford Street", "Bond Street"),
                        4,
                        (2, 4, 7)),
              'Blue': (("Park Lane", "Mayfair"),
                       4,
                       (3, 8)),
              'Black': (("Liverpool Street", "Kings Cross", "Maryleborn", "Fenchurch Street"),
                        2,
                        (1, 2, 3, 4)),
              'White': (("Electric Company", "Water Works"),
                        2,
                        (1, 2))}

'''
card is a cardType
has its own value
it could be a property it need a colour
if its a rent, it need two property colours or All
wild card-could be two colours or all colours
the rest are just action cards

'''

# DeckCards is a global list, consisting of ALL the cards available in a deck.
# Initially we add the lonesone 10M money card
deckCards = [(('Money', 'Money'), 10, None)]

# Used to create a number of the same cards, for example there are 10 Pass Go cards so we call this function
# with howMany=10
def addCards(howMany, cardType, value, colour):
    for counter in range(1, howMany + 1):
        deckCards.append((cardType, value, colour))


def createDeck():
    # Use a loop to add the other money cards which consists of
    # 1@10, 2@5, 5@1, 4@2, 3@3, 2@4
    for value in range(1, 6):
        for counter in range(1, 8-value):
            deckCards.append((('Money', 'Money'), value, None))

    #Create all the different cards using teh above function
    addCards(10, ('Action', 'Pass Go'), 1, None)
    addCards(2, ('Action', 'Deal Breaker'), 5, None)
    addCards(3, ('Action', 'Debt Collector'), 3, None)
    addCards(3, ('Action', 'House'), 3, None)
    addCards(3, ('Action', 'Just Say No'), 4, None)
    addCards(2, ('Action', 'Double The Rent'), 1, None)
    addCards(2, ('Action', 'Hotel'), 4, None)
    addCards(3, ('Action', 'Forced Deal'), 3, None)
    addCards(3, ('Action', 'Sly Deal'), 3, None)
    addCards(3, ('Action', 'It\'s My Birthday'), 2, None)

    addCards(2, ('Wild Card', 'Wild Card'), 0, ('ALL'))
    addCards(1, ('Wild Card', 'Wild Card'), 1, ('Brown', 'Cyan'))
    addCards(1, ('Wild Card', 'Wild Card'), 4, ('Black', 'Cyan'))
    addCards(1, ('Wild Card', 'Wild Card'), 4, ('Green', 'Black'))
    addCards(1, ('Wild Card', 'Wild Card'), 2, ('White', 'Cyan'))
    addCards(1, ('Wild Card', 'Wild Card'), 4, ('Green', 'Blue'))
    addCards(2, ('Wild Card', 'Wild Card'), 3, ('Red', 'Yellow'))
    addCards(2, ('Wild Card', 'Wild Card'), 2, ('Magenta', 'Orange'))

    addCards(2, ('Rent', 'Rent'), 1, ('Brown', 'Cyan'))
    addCards(2, ('Rent', 'Rent'), 1, ('Orange', 'Magenta'))
    addCards(2, ('Rent', 'Rent'), 1, ('Red', 'Yellow'))
    addCards(2, ('Rent', 'Rent'), 1, ('Black', 'White'))
    addCards(2, ('Rent', 'Rent'), 1, ('Green', 'Blue'))

    # Loop around the complex property dictionary structure above and create one of each property card
    for propertyGroup in properties: # i.e. each colour is a group
        # Inner loop iterates through each property in a given colour (which is the outer loop)
        for property in properties[propertyGroup][0]:
            addCards(1, ('Property', property), properties[propertyGroup][1], (propertyGroup))

def shuffleCards():
    # Initialise the deck of cards
    createDeck()

    # Now use some Python magic to shuffle the cards!
    x = [i for i in range(len(deckCards))]
    shuffle(x)

    shuffledDeck = []
    for position in x:
        shuffledDeck.append(deckCards[position])

    return shuffledDeck

# TODO [2] Mia homework: getRentalValue function needed
# I still need that function where I pass in a colour and a number of properties and I return the rent that is payable
# e.g. I have 2 green properties therefore I would have to pay 4 bucks
# HINT look at testCards, try uncommenting the lines and seeing what it does!
# Start of the function done
def getRentalValue(colour, numOfProperties):
    return 0
