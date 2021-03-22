from .context import PokerHands
from .context import Error, NeedHands
import inspect
import unittest


class TestPokerHands(unittest.TestCase):
  """doublet class test cases."""

  def setUp(self):
    ## test deck inputs
    self.pokerhands = PokerHands()
    self.testhands = dict()
    
    self.testhands['Royal flush: ♣'] = ['A♣', 'K♣', '10♣', 'J♣', 'Q♣']
    self.testhands['Straight flush: Q high ♣'] = ['9♣', '8♣', '10♣', 'J♣', 'Q♣']
    self.testhands['Four of a kind: 10'] = ['10♥', '9♥', '10♣', '10♦', '10♠']
    self.testhands['Full house: A and 3'] = ['A♠', 'A♥', '3♣', '3♠', 'A♣']
    self.testhands['Flush: ♥'] = ['6♥', '10♥', 'Q♥', 'K♥', '4♥']
    self.testhands['High card: 10'] = ['6♥', '10♥', '9♦', '8♥', '7♦']
    self.testhands['Three of a kind: 2'] = ['2♥', '9♥', '2♣', '2♦', 'Q♠']
    self.testhands['Two pair: 10 and 9'] = ['10♥', '9♥', '10♣', '9♦', 'Q♠']
    self.testhands['One pair of: A'] = ['A♠', 'A♣', '4♣', '9♦', '8♠']
    self.testhands['High card: K'] = ['6♥', '10♥', 'Q♦', 'K♥', '4♦']

  def testpokerhands_checkTestHands(self):
    #print()
    for handKey in self.testhands:
      theHand = self.testhands[handKey]
      chkStr = self.pokerhands.getHand(theHand)
      #print(chkStr)
      self.assertEqual(handKey, chkStr)

if __name__ == '__main__':
    unittest.main(verbosity=1)
