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

    def makeBid(self, bid):
        '''Change the latest bid.'''
        print (bid.getBidder().getName() + " bets " + str(bid))
        self._lastBid = bid

    def getLastBid(self):
        '''Returns the last bid made in the game.'''
        return self._lastBid

    def callBid(self, caller):
        '''The bid made by the previous player is called.'''
        # Build a mapping of dice face to total shown
        diceFrequencies = dict()
        for player in self.getPlayers():
            diceset = player.getDiceSet()
            print(player.getName() + " reveals: " + str(diceset))
            for dice in diceset:
                diceFrequencies[dice.getTop()] = diceFrequencies.get(
                                                         dice.getTop(), 0) + 1
        # Check whether bid met
        bidCorrect = False
        lastBid = self.getLastBid()
        bidFace = lastBid.getFace()
        if diceFrequencies.get(bidFace, 0) >= lastBid.getFrequency():
            bidCorrect = True
            print("The last bid was correct")
        else:
            print("The last bid was successfully called")

        # Remove a dice for the player who lost and start a new round
        if bidCorrect:
            print(caller.getName() + " loses a dice.")
            caller.removeDice()
            self.playerQueue = self.createPlayerQueue(caller)
        else:
            print(lastBid.getBidder().getName() + " loses a dice.")
            lastBid.getBidder().removeDice()
            self.playerQueue = self.createPlayerQueue(lastBid.getBidder())

    def callSpotOn(self):
        '''The player believes the last bid to be spot on.'''
        pass

    def newRound(self, firstPlayer):
        '''Start a new round from the given player.'''
        self.playerQueue = self.createPlayerQueue(firstPlayer)
        # Get the first player to make a bid
        firstPlayer = self.playerQueue.get()
        self.playerQueue.put(firstPlayer)
        firstPlayer.makeFirstBid()

        # Game loop
        while self.playerQueue.qsize() > 1:
            # Pop player from queue and add to back
            player = self.playerQueue.get()
            self.playerQueue.put(player)
            player.takeTurn()

    def createPlayerQueue(self, firstPlayer):
        '''Creates a queue of players starting with firstPlayer. If any players
        are eliminated then they are removed from the list of players.'''
        queue = Queue()
        queue.put(firstPlayer)
        firstPlayerPosInList = self._playerList.index(firstPlayer)
        for i in range(1, len(self._playerList)):
            player = self._playerList[(firstPlayerPosInList + i) %
                                             len(self._playerList)]
            # Check whether player has been eliminated
            if not player.isEliminated():
                queue.put(player)
            else:
                print(player.getName() + " is eliminated.")
                self._playerList.remove(player)
                i -= 1
        return queue

    def getPlayers(self):
        return self._playerList
