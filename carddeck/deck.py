import random

'''
   test

   from deck import deck
   myD = deck()
   myD.shuffle()

'''

class deck:

  def __init__(self):
    self.sutes = ['︎♠︎','♣︎','♥︎','♦︎']
    self.kind = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    self.cards = []
    for i in self.sutes:
      for j in self.kind:
        self.cards.append(j+i)
    self.deck = self.cards.copy()
  
  def shuffle(self, deck=None):
    if deck is None:
      deck = self.cards.copy()
    # split the deck in two
    cardsindex = list(range(0,len(deck)))
    for i in range(0,100):
      random.shuffle(cardsindex)
    suffleddeck = []
    for i in cardsindex:
      suffleddeck.append(deck[i])
    
    self.deck = suffleddeck.copy()

  def deal(self, cards=5, hands=4):
    if len(self.deck) < cards * hands:
      print('New Deck')
      self.deck = self.cards.copy()
      self.shuffle()
    self.hands = dict()
    for j in range(0,hands):
      self.hands[j] = []
    for i in range(0,cards):
      for j in range(0,hands):
        self.hands[j].append(self.deck.pop(0))  

  def printHands(self):
    '''
    look for poker hands:
      01	Royak fluch
      02	Straight flush
      03	Four of a kind
      04	Full house
      05	Flush
      06	Straight
      07	Three of a kind
      08  Two pair
      09  One pair
      10	High card
    '''
    for i in range(0,len(self.hands)):
      print (self.hands[i])
  

  def __repr__(self):
      return str(self.deck)

  def __str__(self):
      return str(self.deck)