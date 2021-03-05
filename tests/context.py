# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# place class imports belllow
from carddeck.errors import Error, NeedHands
from carddeck.deck import deck