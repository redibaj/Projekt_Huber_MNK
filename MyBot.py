from Player import Player
from Board import Board
import numpy as np
from random import randint

class MyBotRandom(Player):
    def __init__(self, number):
        self.number = number        #1 oder 2, wird bei make_move() als Setzstein übergeben, Spieler markiert mit seiner Nummer auf dem Feld

    def make_move(self, board):
        x_coordinate = randint(1,5)
        y_coordinate = randint(1,5)
        while board.array[x_coordinate - 1][y_coordinate - 1] != 0:
            x_coordinate = randint(1,5)
            y_coordinate = randint(1,5)

        board.set_field_value(y_coordinate, x_coordinate, self.number)
        return board.array
    

