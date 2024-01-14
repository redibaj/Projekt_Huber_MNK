from Player import Player
from Board import Board
import numpy as np
from random import randint


class MyBotRandom(Player):
'''Bot, der nur random Züge spielen kann. '''

    def __init__(self, number):
        self.number = number        

    def make_move(self, board = Board):  
    '''ermöglicht dem Bot das setzen seiner Markierung auf dem Spielfeld-Array.
       2 Pseudo-Zufallszahlen werden erstellt, die für die Indexierung eines Feldes
       verwendet werden. Ist Feld frei, setzt Bot an dieser Stelle. Andernfalls werden
       neue Zufallszahlen generiert, bis der Bot ein leeres Feld trifft''' 
                                        
        x_coordinate = randint(0,4)                                         
        y_coordinate = randint(0,4)                                         
        while board.array[y_coordinate][x_coordinate] != 0:                 #wenn Feld belegt
            x_coordinate = randint(0,4)                                    
            y_coordinate = randint(0,4)                                     

        board.set_field_value(y_coordinate, x_coordinate, self.number)      #methode def. in Board-Klasse, markiert Spielzug auf dem Spielbrett
        return board.array                                                  



class MyBot2(Player):         
'''Bot etwas besser als random'''    

    def __init__(self, number):
        self.number = number
        self.winning_moves_bot2 = []

    def bot2_make_random_move(self, board):          
    '''Bot schaut, ob er mittig auf dem Spielfeld setzen kann. Falls nicht,
       versucht er, den Rand möglichst zu meiden. Der Bot teilt im Terminal mit,
       an welcher Stelle er setzt, platziert seine Markierung und übergibt das aktualisierte Spielfeld
       inklusiver seiner letzten Markierung an die Game-Klasse'''                           
        
        if board.array[2][2] == 0:
            y_coordinate = 2
            x_coordinate = 2   
        else:                     
            all_possible_moves = list(np.argwhere(board.array == 0))         #gibt eine Liste von Tupeln zurück, die alle freien Felder (0) besitzen
            for tupel in all_possible_moves:  
                if 0 not in tupel and 4 not in tupel:
                    y_coordinate = tupel[0]
                    x_coordinate = tupel[1]
                    break
                else:
                    y_coordinate = tupel[0]
                    x_coordinate = tupel[1]
                                                                                             #andere zufällige y-Koordinate wird generiert
        print(f"Bot setzt random hier: {x_coordinate + 1, 5 - y_coordinate}")
        board.set_field_value(y_coordinate, x_coordinate, self.number)                       #methode def. in Board-Klasse, markiert Spielzug auf dem Spielbrett
        return board.array         

    def make_move(self, board):
        self.check_horizontally(board)
        self.check_vertically(board)
        if self.winning_moves_bot2 == []:
            self.bot2_make_random_move(board)
            return board.array
        else:
            random_number = randint(0, len(self.winning_moves_bot2) - 1)
            print(f"mögliche Züge in Array-Index-Form in possible_moves: {self.winning_moves_bot2}")
            print(f"Bot setzt hier: ({self.winning_moves_bot2[random_number][0], self.winning_moves_bot2[random_number][1]})")
            board.set_field_value(self.winning_moves_bot2[random_number][0], self.winning_moves_bot2[random_number][1], self.number)
            self.winning_moves_bot2 = []
            return board.array

    def check_horizontally(self, board):     
    '''überprüft, ob horizontal auf dem Spielfeld 3 Steine in einer Reihe sind.'''                
        for row_index in range(len(board.array)):       
            row = board.array[row_index]               
            for element in range(len(row)):             

                if element == 0 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element+3] == 0:
                        self.winning_moves_bot2.append((row_index, element+3, "h"))

                if element == 2 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element-1] == 0:
                        self.winning_moves_bot2.append((row_index, element-1, "h"))    


    def check_vertically(self, board):       
        transposed_board = np.rot90(board.array)         #flippt das board um 90° -> die Spalten werden zu Zeilen              
        for row_index in range(len(transposed_board)):       #für spätere Indexierung des Arrays für speichern des möglichen Zuges
            row = transposed_board[row_index]                #zur Verbesserung der übersichtlichkeit
            for element in range(len(row)):              #nur elemente in der Reihe
                if element == 0 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element+3] == 0:
                        self.winning_moves_bot2.append((element+3, 4-row_index, "v"))

                if element == 2 or element == 1:
                    if row[element] == row[element+1] == row[element+2] == self.number and row[element-1] == 0:
                        self.winning_moves_bot2.append((element-1, 4-row_index, "v"))                                                             

