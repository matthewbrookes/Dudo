import random

class Dice(object):
    """Represents a six sided fair dice"""

    def __init__(self):
        self.roll()

    def getTop(self):
        """Returns the face shown to the player."""
        return self._top

    def roll(self):
        """Randomises the top face to an int between 1 and 6 inclusive."""
        self._top = random.randint(1, 6)
