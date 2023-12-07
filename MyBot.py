from Player import Player
from Board import Board
import numpy as np
from random import randint

class MyBotRandom(Player):
    def __init__(self, number):
        self.number = number        #1 oder 2, wird bei make_move() als Setzstein übergeben, Spieler markiert mit seiner Nummer auf dem Feld

    def make_move(self, board):
        x_coordinate = randint(0,4)
        y_coordinate = randint(0,4)
        while board.array[y_coordinate][x_coordinate] != 0:
            x_coordinate = randint(0,4)
            y_coordinate = randint(0,4)

        board.set_field_value(y_coordinate, x_coordinate, self.number)
        return board.array

class MyBotReactive(Player):
    possible_moves = []

    def __init__(self, number):
        self.number = number
    
    def make_random_move(self, board):
        x_coordinate = randint(0,4)
        y_coordinate = randint(0,4)
        while board.array[y_coordinate][x_coordinate] != 0:
            x_coordinate = randint(0,4)
            y_coordinate = randint(0,4)

        board.set_field_value(y_coordinate, x_coordinate, self.number)
        return board.array
        
    def make_move(self, board):
        #kein diagonaler Check, weil es muss ja noch Luft nach oben sein :)
        self.check_horizontally()
        self.check_vertically()
        possible_moves = []
        possible_moves.extend(horizontal_moves).extend(vertical_moves)   #fügt alle halbwegs sinnvollen Züge in eine Liste ein
        if possible_moves == []:
            self.make_random_move(board)
        else:
            random_num = randint(0, len(possible_moves))
            board.set_field_value(possible_moves[random_num][0], possible_moves[random_num][1], self.number)     #sucht aus der Liste mit Tuplen ein zufälliges Tupel aus und setzt den Stein an dieser Stelle
            return board.array
        #kein diagonaler Check, weil es muss ja noch Luft nach oben sein :)

    def check_horizontally(self, board):
        horizontal_moves = []
        for row in board.array:                                                       #für jede Reihe in board.array
            for i in range(len(row) -3):                                              #für jedes Element in der Reihe
                if row[i] != 0:                                                       #wenn das Element nicht 0 ist                                         
                    if (row[i] == row[i + 1]):                                        #wenn 4 Elemente in Folge gleich sind
                        if (row[i + 2]) > 4:
                            if row[i-1] == 0:
                                horizontal_moves.append((row, i-1))
                            else:
                                pass
                        else:
                            if (row[i + 2]) == 0:
                                horizontal_moves.append((row, i+2))
                            else:
                                pass
                    else: 
                        pass
                else: 
                    pass
        return horizontal_moves
    
    def check_vertically(self, board):
        vertical_moves = []
        transposed_board = np.transpose(self.array)                     #flippt das board um 90° -> die Spalten werden zu Zeilen                             
        for row in transposed_board:                                                       #für jede Reihe in board.array
            for i in range(len(row) -3):                                              #für jedes Element in der Reihe
                if row[i] != 0:                                                       #wenn das Element nicht 0 ist                                         
                    if (row[i] == row[i + 1]):                                        #wenn 4 Elemente in Folge gleich sind
                        if (row[i + 2]) > 4:
                            if row[i-1] == 0:
                                vertical_moves.append((row, i-1))
                            else:
                                pass
                        else:
                            if (row[i + 2]) == 0:
                                vertical_moves.append((row, i+2))
                            else:
                                pass
                    else: 
                        pass
                else: 
                    pass                                          
        return vertical_moves              


