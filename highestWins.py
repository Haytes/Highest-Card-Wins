from itertools import product
import random

class card(object):



    """docstring for Card."""
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        FACES = ['Jack','Queen','King','Ace']
        if self.value >10:
            return "{0} of {1}".format(FACES[self.value-11],self.suit)
        return "{0} of {1}".format(self.value,self.suit)

    def __lt__(self, other):
        return self.rank < other.rank

class deck(object):
    """docstring for deck."""
    def __init__(self, ranks=None, suits=None):
        if ranks is None:
            ranks = range(2, 15)
        if suits is None:
            suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.deck = []
        self.dealt = []
        for r in ranks:
            for s in suits:
                self.deck.append(card(r, s))

    def draw(self, x):
        while True:
            card = random.sample(self.deck,x)
            if card not in self.dealt:
                self.dealt.append(card)
                return card



def play(deck):

    playerHand = deck.draw(1)
    computerHand = deck.draw(1)
    print("Player Hand:   " + " - ".join(map(str, playerHand)))
    print("Computer Hand:   " + " - ".join(map(str, computerHand)))
    if computerHand[0].value > playerHand[0].value:
        print ("Computer Wins")
    if computerHand[0].value < playerHand[0].value:
        print ("Player Wins")
    if computerHand[0].value == playerHand[0].value:
        print ("Tie Game")
    response = input('To play again enter Y. \n To exit enter any other key.')
    if (response == 'y' or response == 'Y'):
        play(deck)



deck = deck()
play(deck)
