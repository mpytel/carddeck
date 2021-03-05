from .context import deck
from .context import Error
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
    #try:
    with self.assertRaises(NeedMesh):
        thedoublet = doublet(self.strength, self.xd, self.yd)
    #except:
    #  func_name = inspect.stack()[0][3]
    #  print("Run:", func_name, "     FAIL")
    #else:
    #  func_name = inspect.stack()[0][3]
    #  print("Run:", func_name, "     PASS")

  def testdeck_samecardsafterdealandsuffle(self):
    deck01 = self.deck # deck after standard deal in setUP
    deck02 = deck01.copy()
    deck01.shuffle(deck01.deck)
    sameCards = False
    for i in deck02:
      if i not in deck01:
          break
      elif i is tS[-1]:
          sameCards = True

    self.assertEqual(sameCards, True)

if __name__ == '__main__':
    unittest.main(verbosity=1)
