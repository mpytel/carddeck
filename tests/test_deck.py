from .context import deck, cards
from .context import Error, NeedHands
import inspect
import unittest


class TestDeck(unittest.TestCase):
  """doublet class test cases."""

  def setUp(self):
    ## test deck inputs
    self.deck = deck()
    self.deck.shuffle()
    self.deck.deal()

  def testdeck_havehands(self):
    self.assertTrue(len(self.deck.hands) > 0)

  def testdeck_samecardsafterdealandsuffle(self):
    deck01 = self.deck # deck after standard deal in setUP
    someCards = cards()
    deck02 = someCards.getcards()
    deck01.shuffle(deck01.deck)
    sameCards = False
    for i in deck01:
      if i not in deck02:
          print(i)
          break
      else:
          sameCards = True
    self.assertEqual(sameCards, True)

if __name__ == '__main__':
    unittest.main(verbosity=1)
