from Cards import shuffleCards, properties

shuffledDeck = shuffleCards()
#for card in shuffledDeck:
#    print(card)

'''
print(properties)
print(properties['Brown'])
print(properties['Brown'][2])
print(properties['Brown'][2][1])

print(properties['Magenta'][0][1])

for property in properties:
    print(property, properties[property][0][1])
    print(property, len(properties[property][0]), properties[property][0][len(properties[property][0])-1])

for property in properties:
    print(property, properties[property][0][1][0])
    
'''
sum=0
for card in shuffledDeck:
    #print(card[1])
    sum=card[1]+sum
print(sum)

print(shuffledDeck)