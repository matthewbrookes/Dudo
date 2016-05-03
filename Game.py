from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer
from Dice import Dice
from queue import Queue

class Game(object):
    '''Represents a game of Dudo.'''

    def __init__(self, playername):
        # Create a list of players, one human and four computer
        self._playerList = [HumanPlayer(playername, self)]
        for i in range(1, 5):
            self._playerList.append(ComputerPlayer("Computer " + str(i), self))

        # Get the first player
        firstPlayer = self._getFirstPlayer(self._playerList)
        print (firstPlayer.getName() + " gets to go first!")

        # Start the game
        self.newRound(firstPlayer)

    def _getFirstPlayer(self, playerList):
        ''' Returns the first player based on rolling a dice.'''
        highestRollers = set()
        highestRoll = 0
        dice = Dice()
        for player in playerList:
            print(player.getName() + " rolls a " + str(dice.getTop()))
            if dice.getTop() > highestRoll:
                highestRollers.clear()
                highestRollers.add(player)
                highestRoll = dice.getTop()
            elif dice.getTop() == highestRoll:
                highestRollers.add(player)
            dice.roll()
        if len(highestRollers) > 1:
            return self._getFirstPlayer(highestRollers)
        else:
            return highestRollers.pop()

    def makeBid(self, bid, bidder):
        '''Change the latest bid.'''
        print (bidder.getName() + " bets " + str(bid))
        self._lastBid = bid
        self.nextTurn()

    def getLastBid(self):
        '''Returns the last bid made in the game.'''
        return self._lastBid

    def callBid(self):
        '''The bid made by the previous player is called.'''
        pass

    def callSpotOn(self):
        '''The player believes the last bid to be spot on.'''
        pass

    def nextTurn(self):
        '''Play proceeds to the next player.'''
        pass

    def newRound(self, firstPlayer):
        '''Start a new round from the given player.'''
        self.playerQueue = Queue()
        self.playerQueue.put(firstPlayer)
        # Add players to the queue going clockwise from firstPlayer
        firstPlayerPosInList = self._playerList.index(firstPlayer)
        for i in range(1, len(self._playerList)):
            player = self._playerList[(firstPlayerPosInList + i) %
                                             len(self._playerList)]
            # Check whether player has been eliminated
            if not player.isEliminated():
                self.playerQueue.put(player)
            else:
                print(player.getName() + " is eliminated ")
                self._playerList.remove(player)
                i -= 1
        # Get the first player to make a bid
        firstPlayer = self.playerQueue.get()
        self.playerQueue.put(firstPlayer)
        firstPlayer.makeFirstBid()

    def getPlayers(self):
        return self._playerList
