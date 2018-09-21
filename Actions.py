"""
TODO:
Banking money and moving properties to the property pile are not covered here.
For properties (and the property pile) wild cards and houses/hotels can be added. This is also not covered here
Pass go also not covered here
As is Just say no


Action cards consist of
    It's my birthday - all players pay you 2M
    Any rent - one player pays you any choice
    Rent - all players pay you based on the colour and properties
    Double the rent - must be played with a rent card
    Deal Breaker - Steal a full set of properties from one player
    Debt collector - Demand 5M from one player
    Forced deal - swap one of your properties with someone else's
    Sly Deal - steal a property from one other player - can't be from a full set

Summary actions
    You (or all of you) pay me some money
    You give me a/many properties
    You and I swap a property

Abstract action
    Move a card from one pile into someone else's
    Move a card into the discard pile
"""

def moveCardFromPlayerToPlayer(fromPlayerPile, toPlayerPile, cardNum):
    toPlayerPile.append(fromPlayerPile[cardNum])
    fromPlayerPile.remove(fromPlayerPile[cardNum])
