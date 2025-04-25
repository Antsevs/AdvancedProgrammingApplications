class Card:
    SUITS = {1: 'Clubs', 2: 'Hearts', 3: 'Spades', 4: "Diamonds"}
    VALUES = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King'}

    def __init__(self, name):
        from random import randint
        self.v = randint(1,13)
        self.s = randint(1,4)

        print('{}, you have the {} of {}'.format(name, Card.VALUES[self.v], Card.SUITS[self.s]))


card1 = Card('Anthony')
card2 = Card('Jaden')
card3 = Card('Justin')
