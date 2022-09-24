# DiceSet.py
#
# A simple class to simulate a handfull of dice.
#
# Samuel Leming
# 02/12/2001
#
# 02/15/2001 - Added testing to filter out negative numbers.
#              Switched roll to return the more basic ResultList rather than total.

import random
from operator import add

OneSideError = "A die with only one side is a sphere."
NoSidesError = "A die with no sides can't exist."
NegSidesError = "A die can't have negative sides."
NoDiceError = "Why bother rolling zero dice?"
NegDiceError = "You can't roll negative dice."

class DiceSet:
    """Should behave as a handful of dice of all the same type.
    
Ability to average results, drop lowest or highest roll, and use dice
different sides will be added later."""

    def __init__(self):
        """Just a constructor."""
        
        self.ResultList = []
        self.Total = None

    def roll(self, NumDice = 1, Sides = 6):
        """roll(NumDice, Sides) -> Total"""
        
        self.ResultList = []
        if Sides == 0:
            raise NoSidesError
        elif Sides == 1:
            raise OneSideError
        elif Sides < 0:
            raise NegSidesError
        elif NumDice == 0:
            raise NoDiceError
        elif NumDice < 0:
            raise NegDiceError
        self.NumDice = NumDice
        self.Sides = Sides
        for i in range(self.NumDice):
            self.ResultList.append(random.choice(range(self.Sides)) + 1)
        self.Total = reduce(add, self.ResultList)
        return self.ResultList

# This will need to be more complete as the feature list grows.
def test():
    """Tests initiating the object, making the roll, and printing the results. """
    
    TestDice = DiceSet()
    TestDice.roll(20, 6)
    print TestDice.ResultList
    print TestDice.Total

if __name__ == '__main__':
    test()

