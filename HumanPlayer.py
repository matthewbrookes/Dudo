from Player import Player
from Bid import Bid

class HumanPlayer(Player):
    '''Represents a human player at the terminal'''

    def makeFirstBid(self):
        print("Your dice are: " + str(self._diceset))
        validBid = False
        while not validBid:
            print("Please make a bid of the form f d where d is the " +
                    "dice face and f is the number facing up.")
            print("For example a bid of three 4s would be 3 4.")
            bid = input()
            splitbid = bid.split(' ')
            if len(splitbid) == 2:
                if splitbid[0].isnumeric() and splitbid[1].isnumeric():
                    proposedBid = Bid(int(splitbid[1]), int(splitbid[0]))
                    if Bid(0, 0).isValidBid(proposedBid):
                        self.getGame().makeBid(proposedBid, self)
                        validBid = True
                    else :
                        print("That's not a valid bid, you must bid " +
                                "a higher dice value, more of the same " +
                                "dice or both.")

    def takeTurn(self):
        pass
