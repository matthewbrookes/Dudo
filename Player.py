from abc import ABCMeta, abstractmethod
from Dice import Dice

class Player(object):
    """An abstract Dudo player"""

    __metaclass__ = ABCMeta

    def __init__(self, name):
        self._name = name
        # Create a set of five dice
        self._diceset = set()
        self._diceset.add(Dice())
        self._diceset.add(Dice())
        self._diceset.add(Dice())
        self._diceset.add(Dice())
        self._diceset.add(Dice())

    def getName(self):
        """Returns the players name."""
        return self._name

    def getDiceSet(self):
        """Return the set of dice belonging to player."""
        return self._diceset

    def removeDice(self):
        """Returns the set of dice after one is removed."""
        self._diceset.pop()
        return self._diceset

    def addDice(self):
        """Returns the set of dice after one is added.

        Player cannot have more than five dice."""
        if len(self._diceset) < 5:
            self._diceset.add(Dice())
        return self._diceset

    def rollAllDice(self):
        """Rolls all dice belonging to player."""
        for dice in self._diceset:
            dice.roll()

    def isEliminated(self):
        """Returns true iff the player has no dice left."""
        return len(self._diceset) == 0

    @abstractmethod
    def takeTurn(self):
        """Returns the bid made by the player."""
        pass

    def __repr__(self):
        return self._name + str(self._diceset)
