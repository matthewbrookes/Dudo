from Player import Player
from Bid import Bid
import random

class ComputerPlayer(Player):
    """ An AI Dudo player """

    def makeFirstBid(self):
        totalDiceInGame = 0
        game = self.getGame()
        for player in game.getPlayers():
            totalDiceInGame += len(player.getDiceSet())
        avgDicePerPlayer = totalDiceInGame / len(game.getPlayers())
        randomFrequency = random.randint(1, avgDicePerPlayer)
        randomFace = self.getDiceSet().pop()
        self.getDiceSet().add(randomFace)
        self.getGame().makeBid(Bid(randomFace, randomFrequency), self)
