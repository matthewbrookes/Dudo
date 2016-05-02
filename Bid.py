class Bid(object):
    """Represents a bid made by a player"""

    def __init__(self, face, frequency):
        """Creates a bid of specified frequency for specified dice face."""
        self._face = face
        self._frequency = frequency

    def getFace(self):
        """Returns the dice face of this bid."""
        return self._face

    def getFrequency(self):
        """Returns the bidded frequency."""
        return self._frequency

    def isValidBid(self, bid):
        """Returns true iff the supplied bid is valid compared to current bid.

        A valid bid increases the face, frequency or both."""
        if bid.getFace() < 1 or bid.getFace() > 6:
            return False
        elif bid.getFrequency < 1:
            return False
        elif bid.getFace() > self._face:
            return True
        elif bid.getFrequency() > self._frequency:
            return True
        else:
            return False

    def __repr__(self):
        if self.getFrequency() > 1:
            return str(self.getFrequency()) + " " + str(self.getFace()) + "s"
        else:
            return str(self.getFrequency()) + " " + str(self.getFace())
