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
                    proposedBid = Bid(int(splitbid[1]), int(splitbid[0]), self)
                    if Bid(1, 0, self).isValidBid(proposedBid):
                        self.getGame().makeBid(proposedBid)
                        validBid = True
                    else :
                        print("That's not a valid bid, you must bid " +
                                "a higher dice value, more of the same " +
                                "dice or both.")

    def takeTurn(self):
        print("Your dice are: " + str(self._diceset))
        choice = ''
        while choice != 'b' and choice != 'c' and choice != 's':
            print("Would you like to make a bid (b), " +
                  "call the last bid (c) or " +
                  "declare the last bid spot on (s)?")
            choice = input()
        if choice == 'b':
            validBid = False
            while not validBid:
                print("Please make a bid of the form f d where d is the " +
                      "dice face and f is the number facing up.")
                print("For example a bid of three 4s would be 3 4.")
                bid = input()
                if len(bid) == 3:
                    if bid[0].isnumeric() and bid[2].isnumeric():
                        proposedBid = Bid(int(bid[2]), int(bid[0]), self)
                        if self.getGame().getLastBid().isValidBid(proposedBid):
                            self.getGame().makeBid(proposedBid)
                            validBid = True
                        else :
                            print("That's not a valid bid, you must bid " +
                                  "a higher dice value, more of the same " +
                                  "dice or both.")
        elif choice == 'c':
            self.getGame().callBid(self)
