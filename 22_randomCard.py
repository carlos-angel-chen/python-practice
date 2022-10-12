import random

cardsPalo = ['Diamond', 'Spades', 'Hearts', 'Clubs']
ranksNum = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

def pickCard():
    card = random.choice(cardsPalo)
    rank = random.choice(ranksNum)
    return card, rank

palo, carta = pickCard()
print(str(carta) + ' ' + palo)