import sys

cardType = ("cash", "property", "wildcard", "dealbreaker")


deck = [(x, y) for x in [1,2,3] for y in cardType]

print(deck)

